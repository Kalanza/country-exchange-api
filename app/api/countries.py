from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.models.country import Country
from app.schemas.country import CountryResponse
from app.services.refresh import refresh_countries

router = APIRouter(prefix="/countries", tags=["Countries"])

@router.post("/refresh")
def refresh(db: Session = Depends(get_db)):
    status = refresh_countries(db)
    if not status:
        raise HTTPException(status_code=503, detail="External data source unavailable")
    return {"message": "Data refreshed successfully"}

@router.get("/", response_model=List[CountryResponse])
def list_countries(region: str = None, currency: str = None, sort: str = None, db: Session = Depends(get_db)):
    query = db.query(Country)

    if region:
        query = query.filter(Country.region == region)

    if currency:
        query = query.filter(Country.currency_code == currency)

    if sort == "gdp_desc":
        query = query.order_by(Country.estimated_gdp.desc())
    elif sort == "gdp_asc":
        query = query.order_by(Country.estimated_gdp.asc())

    return query.all()

@router.get("/{name}", response_model=CountryResponse)
def get_country(name: str, db: Session = Depends(get_db)):
    country = db.query(Country).filter(Country.name.ilike(name)).first()
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country

@router.delete("/{name}")
def delete_country(name: str, db: Session = Depends(get_db)):
    country = db.query(Country).filter(Country.name.ilike(name)).first()
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    db.delete(country)
    db.commit()
    return {"message": f"{name} deleted"}
