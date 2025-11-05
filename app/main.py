from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.countries import router as country_router

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Country Currency Exchange API",
    description="An API for country information and exchange rates",
    version="1.0.0"
)

app.include_router(country_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Country Currency Exchange API"}

@app.get("/status")
async def status():
    return {"status": "running"}
