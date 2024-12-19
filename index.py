import pandas as pd
import random
import os
from faker import Faker

fake = Faker()
random.seed(42)

os.makedirs("data", exist_ok=True)

products = []
categories = ["Elektronika", "Moda", "Dom i ogród", "Sport", "Zabawki"]
for i in range(1, 101):
    products.append({
        "product_id": i,
        "name": fake.word().capitalize(),
        "category": random.choice(categories),
        "price": round(random.uniform(10.0, 500.0), 2)
    })
products_df = pd.DataFrame(products)
products_df.to_csv("data/products.csv", index=False)

merchants = []
for i in range(1, 21):
    merchants.append({
        "merchant_id": i,
        "name": fake.company(),
        "location": fake.city()
    })
merchants_df = pd.DataFrame(merchants)
merchants_df.to_csv("data/merchants.csv", index=False)

sales = []
for i in range(1, 1001):
    sales.append({
        "transaction_id": i,
        "product_id": random.randint(1, 100),
        "merchant_id": random.randint(1, 20),
        "quantity": random.randint(1, 10),
        "transaction_date": fake.date_between(start_date="-1y", end_date="today"),
        "price": round(random.uniform(10.0, 500.0), 2)
    })
sales_df = pd.DataFrame(sales)
sales_df.to_csv("data/sales.csv", index=False)

reviews = []
for i in range(1, 501):
    reviews.append({
        "review_id": i,
        "product_id": random.randint(1, 100),
        "rating": random.randint(1, 5),
        "review_text": fake.sentence(),
        "review_date": fake.date_between(start_date="-1y", end_date="today")
    })
reviews_df = pd.DataFrame(reviews)
reviews_df.to_csv("data/reviews.csv", index=False)

print("Dane testowe zostały wygenerowane i zapisane do folderu 'data/'.")
