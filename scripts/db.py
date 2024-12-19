from sqlalchemy import create_engine

DB_NAME = "ecommerce"
DB_USER = "postgres"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = 5432

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
