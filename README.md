# ETL Currency Exchange Pipeline

This project demonstrates an end-to-end ETL pipeline that:
- Extracts static currency codes from a CSV file
- Extracts live exchange rates from an API
- Transforms and merges the data
- Loads the final dataset into a Microsoft SQL Server database

## Tools Used
- Python
- Pandas
- SQLAlchemy
- Microsoft SQL Server Express
- ODBC Driver 18

## How to Run
1. Ensure SQL Server is running and accessible.
2. Update credentials in `elt_pipeline.py`.
3. Run: `python elt_pipeline.py`

## Output
All data is loaded into the `ExchangeRates` table in your database.

