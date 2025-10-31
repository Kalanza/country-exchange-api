from fastapi import FastAPI

app = FastAPI(
    title="Country Exchange API",
    description="An API for country information",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to Country Exchange API"}

@app.get("/status")
async def status():
    return {"status": "running"}
