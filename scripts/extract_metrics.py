import pandas as pd

from scripts.db import engine

queries = {
    "total_sales_per_merchant": """
        SELECT merchant_id, SUM(price * quantity) AS total_sales
        FROM sales
        GROUP BY merchant_id
        ORDER BY total_sales DESC;
    """,
    "top_selling_products": """
        SELECT product_id, SUM(quantity) AS total_sold
        FROM sales
        GROUP BY product_id
        ORDER BY total_sold DESC
        LIMIT 5;
    """,
    "monthly_revenue_trends": """
        SELECT DATE_TRUNC('month', transaction_date) AS month, SUM(price * quantity) AS monthly_revenue
        FROM sales
        GROUP BY month
        ORDER BY month;
    """
}

output_dir = "data/processed"

def extract_and_save(query_name, query):
    """Run a query, save the results to a CSV file."""
    print(f"Running query: {query_name}")
    df = pd.read_sql_query(query, engine)
    output_path = f"{output_dir}/{query_name}.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved {query_name} to {output_path}")

def main():
    for query_name, query in queries.items():
        extract_and_save(query_name, query)

if __name__ == "__main__":
    main()
