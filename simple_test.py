import requests
import time

time.sleep(1)

try:
    print("Testing root endpoint...")
    r = requests.get("http://127.0.0.1:8000/", timeout=5)
    print(f"Root: {r.status_code} - {r.text[:100]}")
    
    print("Testing status endpoint...")
    r = requests.get("http://127.0.0.1:8000/status", timeout=5)
    print(f"Status: {r.status_code} - {r.text[:100]}")
    
    print("Testing countries endpoint...")
    r = requests.get("http://127.0.0.1:8000/countries", timeout=5)
    print(f"Countries: {r.status_code}")
    if r.status_code == 200:
        print(f"  Count: {len(r.json())}")
    else:
        print(f"  Error: {r.text[:200]}")
        
except Exception as e:
    print(f"Error: {e}")
