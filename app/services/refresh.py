import random
from datetime import datetime
from sqlalchemy.orm import Session
from app.services.country_fetcher import fetch_countries
from app.services.exchange_fetcher import fetch_exchange_rates
from app.models.country import Country

def refresh_countries(db: Session):
    country_data = fetch_countries()
    rates = fetch_exchange_rates()

    if not country_data or not rates:
        return None  

    for c in country_data:
        rate = rates.get(c["currency_code"], None) if c["currency_code"] else None
        
        estimated_gdp = None
        if rate and rate > 0:
            multiplier = random.randint(1000, 2000)
            estimated_gdp = (c["population"] * multiplier) / rate

        existing = db.query(Country).filter(Country.name == c["name"]).first()

        if existing:
            existing.capital = c["capital"]
            existing.region = c["region"]
            existing.population = c["population"]
            existing.currency_code = c["currency_code"]
            existing.exchange_rate = rate
            existing.estimated_gdp = estimated_gdp
            existing.flag_url = c["flag_url"]
            existing.last_refreshed_at = datetime.utcnow()
        else:
            new_entry = Country(
                name=c["name"],
                capital=c["capital"],
                region=c["region"],
                population=c["population"],
                currency_code=c["currency_code"],
                exchange_rate=rate,
                estimated_gdp=estimated_gdp,
                flag_url=c["flag_url"],
                last_refreshed_at=datetime.utcnow()
            )
            db.add(new_entry)

    db.commit()
    return True
