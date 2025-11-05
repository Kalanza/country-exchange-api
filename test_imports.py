import sys
print("Python path:", sys.path)

try:
    print("Importing FastAPI...")
    from fastapi import FastAPI
    print("✓ FastAPI imported")
    
    print("Loading .env...")
    from dotenv import load_dotenv
    load_dotenv()
    print("✓ .env loaded")
    
    print("Importing country router...")
    from app.api.countries import router as country_router
    print("✓ Country router imported")
    
    print("Creating app...")
    app = FastAPI()
    print("✓ App created")
    
    print("Including router...")
    app.include_router(country_router)
    print("✓ Router included")
    
    print("\nAll imports successful!")
    
except Exception as e:
    import traceback
    print(f"\n✗ Error: {e}")
    traceback.print_exc()
