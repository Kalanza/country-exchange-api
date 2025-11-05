import requests
import json

BASE_URL = "http://localhost:8000"

print("=" * 50)
print("Testing Country Exchange API")
print("=" * 50)

# Test 1: GET /
print("\n1. Testing GET / (root)")
response = requests.get(f"{BASE_URL}/")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

# Test 2: GET /status
print("\n2. Testing GET /status")
response = requests.get(f"{BASE_URL}/status")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

# Test 3: GET /countries (should be empty initially)
print("\n3. Testing GET /countries (before refresh)")
response = requests.get(f"{BASE_URL}/countries")
print(f"Status: {response.status_code}")
if response.status_code == 200:
    print(f"Count: {len(response.json())}")
else:
    print(f"Error: {response.text}")

# Test 4: POST /countries/refresh
print("\n4. Testing POST /countries/refresh")
response = requests.post(f"{BASE_URL}/countries/refresh")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

# Test 5: GET /countries (after refresh)
print("\n5. Testing GET /countries (after refresh)")
response = requests.get(f"{BASE_URL}/countries")
print(f"Status: {response.status_code}")
data = response.json()
print(f"Count: {len(data)}")
if data:
    print(f"First country: {data[0]['name']}")

# Test 6: GET /countries?region=Africa
print("\n6. Testing GET /countries?region=Africa")
response = requests.get(f"{BASE_URL}/countries", params={"region": "Africa"})
print(f"Status: {response.status_code}")
print(f"Africa count: {len(response.json())}")

# Test 7: GET /countries?sort=gdp_desc
print("\n7. Testing GET /countries?sort=gdp_desc")
response = requests.get(f"{BASE_URL}/countries", params={"sort": "gdp_desc"})
print(f"Status: {response.status_code}")
data = response.json()
if data:
    print(f"First (highest GDP): {data[0]['name']} - GDP: {data[0]['estimated_gdp']}")

# Test 8: GET /countries/{name}
print("\n8. Testing GET /countries/{{name}} (first country)")
response = requests.get(f"{BASE_URL}/countries")
if response.json():
    first_country_name = response.json()[0]['name']
    response = requests.get(f"{BASE_URL}/countries/{first_country_name}")
    print(f"Status: {response.status_code}")
    print(f"Country: {response.json()['name']}")

print("\n" + "=" * 50)
print("All tests completed!")
print("=" * 50)
