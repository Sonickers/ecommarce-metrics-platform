import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

sales_data = pd.read_csv("../data/processed/total_sales_per_merchant.csv")
products_data = pd.read_csv("../data/processed/top_selling_products.csv")
revenue_data = pd.read_csv("../data/processed/monthly_revenue_trends.csv")

st.title("E-Commerce Metrics Dashboard")

st.header("Total Sales Per Merchant")
st.bar_chart(sales_data.set_index("merchant_id")["total_sales"])

st.header("Top-Selling Products")
fig, ax = plt.subplots()
ax.pie(
    products_data['total_sold'],
    labels=products_data['product_id'],
    autopct='%1.1f%%',
    startangle=140
)
ax.set_title("Top-Selling Products")
st.pyplot(fig)

st.header("Monthly Revenue Trends")
revenue_data['month'] = pd.to_datetime(revenue_data['month'])
st.line_chart(revenue_data.set_index("month")["monthly_revenue"])
