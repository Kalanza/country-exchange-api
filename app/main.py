from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.db import get_db
from app.models.country import Country
from app.api.countries import router as country_router

app = FastAPI(title="Country Currency Exchange API")

app.include_router(country_router)

@app.get("/status")
def status(db: Session = Depends(get_db)):
    count = db.query(Country).count()
    last_country = db.query(Country).order_by(Country.last_refreshed_at.desc()).first()
    last_refreshed = last_country.last_refreshed_at if last_country else None

    return {
        "total_countries": count,
        "last_refreshed_at": last_refreshed,
        "timestamp": datetime.utcnow(),
    }
