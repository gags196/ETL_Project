# config.py

DB_CONFIG = {
    "server": "MSI\\SQLEXPRESS",           # From SSMS Object Explorer
    "database": "ETLDB",                   # Your target database
    "username": "etl_user",                # Your SQL login
    "password": "StrongPassword123",       # Its password
    "driver": "ODBC Driver 18 for SQL Server"
}

# Path to your input CSV (must have Country,Code columns)
CSV_PATH = "data/currency_countries.csv"

# Exchange‐rate API endpoint
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Name of the table to write into
TABLE_NAME = "ExchangeRates"
