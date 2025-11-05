# Country Exchange API

A FastAPI-based REST API for retrieving country information and exchange rates. This application fetches real-time data from public APIs and provides endpoints to query, filter, and manage country data.

## Features

- 🌍 **Country Information** - Retrieve details about countries including capital, region, population, and currency
- 💱 **Exchange Rates** - Get real-time exchange rates for different currencies
- 📊 **GDP Estimation** - Calculate estimated GDP based on population and exchange rates
- 🔍 **Advanced Filtering** - Filter countries by region or currency
- 📈 **Sorting** - Sort countries by GDP (ascending or descending)
- 🔄 **Data Refresh** - Sync country data with external sources
- 📚 **Interactive API Docs** - Swagger UI and ReDoc documentation

## Tech Stack

- **Framework:** FastAPI
- **Server:** Uvicorn
- **Database:** SQLite with SQLAlchemy ORM
- **Migrations:** Alembic
- **Configuration:** Pydantic Settings

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kalanza/country-exchange-api.git
   cd country-exchange-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r app/requirements.txt
   ```

4. **Create .env file**
   ```bash
   echo 'DATABASE_URL=sqlite:///./country_exchange.db' > .env
   ```

5. **Initialize the database**
   ```bash
   cd app
   alembic upgrade head
   ```

## Running the Server

### Development Mode
```bash
uvicorn app.main:app --reload --port 8000
```

### Production Mode
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check
- **GET** `/` - Welcome message
- **GET** `/status` - Server status

### Countries
- **GET** `/countries` - List all countries
  - Query Parameters:
    - `region` (optional) - Filter by region (e.g., Africa, Europe)
    - `currency` (optional) - Filter by currency code (e.g., USD, EUR)
    - `sort` (optional) - Sort by GDP (values: `gdp_desc`, `gdp_asc`)

- **GET** `/countries/{name}` - Get specific country details
  - Path Parameters:
    - `name` - Country name (case-insensitive)

- **POST** `/countries/refresh` - Refresh country data from external APIs

- **DELETE** `/countries/{name}` - Delete a country from database
  - Path Parameters:
    - `name` - Country name (case-insensitive)

## Example Usage

### Get all countries
```bash
curl http://localhost:8000/countries
```

### Filter by region
```bash
curl "http://localhost:8000/countries?region=Africa"
```

### Sort by GDP (descending)
```bash
curl "http://localhost:8000/countries?sort=gdp_desc"
```

### Get single country
```bash
curl http://localhost:8000/countries/Nigeria
```

### Refresh data
```bash
curl -X POST http://localhost:8000/countries/refresh
```

### Delete country
```bash
curl -X DELETE http://localhost:8000/countries/Nigeria
```

## Interactive API Documentation

Once the server is running, visit:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

You can test all endpoints directly from the browser!

## Project Structure

```
country-exchange-api/
├── app/
│   ├── api/
│   │   └── countries.py          # Country routes
│   ├── models/
│   │   └── country.py            # SQLAlchemy Country model
│   ├── schemas/
│   │   └── country.py            # Pydantic response schemas
│   ├── services/
│   │   ├── country_fetcher.py    # Fetch country data from API
│   │   ├── exchange_fetcher.py   # Fetch exchange rates from API
│   │   └── refresh.py            # Data refresh logic
│   ├── alembic/                  # Database migrations
│   ├── config.py                 # Configuration settings
│   ├── db.py                     # Database setup
│   ├── main.py                   # FastAPI app initialization
│   └── requirements.txt          # Dependencies
├── .env                          # Environment variables (not committed)
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=sqlite:///./country_exchange.db
BASE_CURRENCY=USD
```

## External APIs Used

### Country Data
- **URL:** https://restcountries.com/v2/all
- **Type:** Public API (No authentication required)
- **Rate Limit:** Generous

### Exchange Rates
- **URL:** https://open.er-api.com/v6/latest/{currency}
- **Type:** Public API (No authentication required)
- **Rate Limit:** Free tier available

## Database Schema

### Countries Table
- `id` - Primary key
- `name` - Country name (unique)
- `capital` - Capital city
- `region` - Geographic region
- `population` - Country population
- `currency_code` - ISO currency code
- `exchange_rate` - Exchange rate to USD
- `estimated_gdp` - Calculated GDP estimate
- `flag_url` - Country flag image URL
- `last_refreshed_at` - Last update timestamp

## Error Handling

The API returns standard HTTP status codes:

- `200 OK` - Successful request
- `400 Bad Request` - Invalid parameters
- `404 Not Found` - Country not found
- `500 Internal Server Error` - Server error
- `503 Service Unavailable` - External data source unavailable

## Security

- ✅ No hardcoded credentials
- ✅ All secrets loaded from environment variables
- ✅ Database files excluded from version control
- ✅ Public APIs only (no private keys)
- ✅ Proper `.gitignore` configuration

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Author

Created by [Kalanza](https://github.com/Kalanza)

---

**Last Updated:** November 5, 2025
