import pandas as pd
import matplotlib.pyplot as plt
import os

processed_data_dir = "../data/processed"
output_dir = "../dashboards"

os.makedirs(output_dir, exist_ok=True)

def plot_total_sales_per_merchant():
    """Bar chart for total sales per merchant."""
    file_path = f"{processed_data_dir}/total_sales_per_merchant.csv"
    df = pd.read_csv(file_path)

    plt.figure(figsize=(10, 6))
    plt.bar(df['merchant_id'], df['total_sales'], color='skyblue')
    plt.title("Total Sales Per Merchant", fontsize=16)
    plt.xlabel("Merchant ID", fontsize=12)
    plt.ylabel("Total Sales ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/total_sales_per_merchant.png")
    plt.show()

def plot_top_selling_products():
    """Pie chart for top-selling products."""
    file_path = f"{processed_data_dir}/top_selling_products.csv"
    df = pd.read_csv(file_path)

    plt.figure(figsize=(8, 8))
    plt.pie(
        df['total_sold'],
        labels=df['product_id'],
        autopct='%1.1f%%',
        startangle=140
    )
    plt.title("Top-Selling Products", fontsize=16)
    plt.savefig(f"{output_dir}/top_selling_products.png")
    plt.show()

def plot_monthly_revenue_trends():
    """Line chart for monthly revenue trends."""
    file_path = f"{processed_data_dir}/monthly_revenue_trends.csv"
    df = pd.read_csv(file_path)

    df['month'] = pd.to_datetime(df['month'])

    plt.figure(figsize=(12, 6))
    plt.plot(df['month'], df['monthly_revenue'], marker='o', linestyle='-', color='green')
    plt.title("Monthly Revenue Trends", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Revenue ($)", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/monthly_revenue_trends.png")
    plt.show()

if __name__ == "__main__":
    plot_total_sales_per_merchant()
    plot_top_selling_products()
    plot_monthly_revenue_trends()