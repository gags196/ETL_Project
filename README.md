# 📌 Project Title: ETL Pipeline for Currency Exchange Rate Integration

## 🧩 Description
This project demonstrates a basic ETL (Extract, Transform, Load) pipeline that extracts country-currency mapping data from a CSV file and real-time currency exchange rates via an API. It transforms and integrates the data, then loads it into a Microsoft SQL Server database.

## 🗂️ Project Structure

```
ETL_Currency_Pipeline/
├── country_currency.csv       # Input CSV with country and currency codes
├── config.py                  # Contains DB connection and API config
├── elt_pipeline.py            # Main ETL pipeline script
├── etl_log.log                # Log file recording ETL activity
├── README.md                  # Project documentation
```

## ⚙️ Setup Instructions

### 1. Prerequisites
- Python 3.8+
- Microsoft SQL Server (Express or full version)
- Microsoft ODBC Driver 18 for SQL Server
- Python packages: `pandas`, `sqlalchemy`, `requests`, `pyodbc`

### 2. Install Dependencies

```bash
pip install pandas sqlalchemy requests pyodbc
```

### 3. Prepare SQL Server
- Create a database named `CurrencyDB`
- Enable TCP/IP protocol in SQL Server Configuration Manager
- Create a user `etl_user` with the specified password and grant access to `CurrencyDB`


## 🚀 Running the Pipeline

```bash
python elt_pipeline.py
```

- The script:
  - Extracts country-currency mappings from `country_currency.csv`
  - Fetches latest exchange rates from an external API
  - Merges the datasets and loads them into the `ExchangeRates` table in SQL Server
  - Logs progress in `etl_log.log`

## 📈 KPI Highlights
- Automated data extraction and transformation from CSV and API.
- Reduced manual data integration efforts with scheduled ETL logic.
- Ensured data reliability via logging and exception handling.
- Connected Python and SQL Server using `SQLAlchemy` and `pyodbc`.
