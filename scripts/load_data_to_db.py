import os
import pandas as pd

from scripts.db import engine


RAW_DATA_DIR = os.path.join("..", "data", "raw")
CSV_FILES = {
    "products": "products.csv",
    "merchants": "merchants.csv",
    "sales": "sales.csv",
    "reviews": "reviews.csv",
}

def load_csv_to_table(csv_file, table_name):
    """Loads a CSV file into a PostgreSQL table."""
    file_path = os.path.join(RAW_DATA_DIR, csv_file)
    try:
        print(f"Loading {file_path} into {table_name}...")
        df = pd.read_csv(file_path)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Successfully loaded {table_name}!")
    except Exception as e:
        print(f"Error loading {table_name}: {e}")

def main():
    for table, csv_file in CSV_FILES.items():
        load_csv_to_table(csv_file, table)

if __name__ == "__main__":
    main()
