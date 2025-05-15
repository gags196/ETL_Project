import pandas as pd
import requests
import logging
import urllib.parse
from sqlalchemy import create_engine
from config import DB_CONFIG, CSV_PATH, API_URL, TABLE_NAME

# ——— Logging Setup ——————————————————————————————————
logging.basicConfig(
    filename="etl_log.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# ——— Extract ——————————————————————————————————————  
def extract_csv(path):
    try:
        df = pd.read_csv(path)
        logging.info(f"CSV extracted: {len(df)} rows.")
        return df
    except Exception as e:
        logging.error(f"CSV extraction error: {e}")
        return pd.DataFrame()

def extract_api(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json().get("rates", {})
        df = pd.DataFrame(list(data.items()), columns=["Code", "Rate"])
        logging.info(f"API extracted: {len(df)} rates.")
        return df
    except Exception as e:
        logging.error(f"API extraction error: {e}")
        return pd.DataFrame()

# ——— Transform —————————————————————————————————————  
def transform_data(csv_df, api_df):
    if csv_df.empty or api_df.empty:
        logging.warning("One or both DataFrames are empty – skipping transform.")
        return pd.DataFrame()

    # Standardize column names & cases
    csv_df = csv_df.rename(columns={"Code": "Code", "Country": "Country"})
    csv_df["Code"] = csv_df["Code"].str.upper()
    api_df["Code"] = api_df["Code"].str.upper()

    # Debug: peek at the heads
    print("CSV head:\n", csv_df.head(), "\nAPI head:\n", api_df.head())

    merged = pd.merge(csv_df, api_df, on="Code", how="inner")
    logging.info(f"Transformed: {len(merged)} rows after merge.")
    return merged

# ——— Load —————————————————————————————————————————  
def load_to_sql_server(df):
    if df.empty:
        logging.warning("No data to load.")
        return

    # Build ODBC connection string with driver 18 and trust cert
    conn_str = (
        f"DRIVER={{{DB_CONFIG['driver']}}};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['username']};"
        f"PWD={DB_CONFIG['password']};"
        f"TrustServerCertificate=yes;Encrypt=no;"
    )
    quoted = urllib.parse.quote_plus(conn_str)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={quoted}")

    try:
        df.to_sql(TABLE_NAME, con=engine, if_exists="replace", index=False)
        logging.info(f"Loaded into table `{TABLE_NAME}` successfully.")
    except Exception as e:
        logging.error(f"Load error: {e}")

# ——— Main Flow —————————————————————————————————————  
def run_etl():
    csv_df = extract_csv(CSV_PATH)
    api_df = extract_api(API_URL)
    final_df = transform_data(csv_df, api_df)
    load_to_sql_server(final_df)

if __name__ == "__main__":
    run_etl()
