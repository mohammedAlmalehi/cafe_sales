
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Qahwa Corner Dashboard",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Qahwa Corner Sales Dashboard")
st.write("Coffee Shop Sales Analysis - 2026")

# Load dataset
df = pd.read_csv("cafe_sales.csv")

# Prepare data
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['total_sar'] = pd.to_numeric(df['total_sar'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

df = df.dropna(subset=['branch', 'product', 'total_sar', 'quantity'])

# Branch selector
branches = ["All Branches"] + sorted(df['branch'].dropna().unique().tolist())

selected_branch = st.sidebar.selectbox(
    "Select Branch",
    branches
)

if selected_branch != "All Branches":
    filtered_df = df[df['branch'] == selected_branch]
else:
    filtered_df = df

# Revenue metric
total_revenue = filtered_df['total_sar'].sum()

st.metric(
    label="Total Revenue (SAR)",
    value=f"{total_revenue:,.2f}"
)

# Revenue by product
st.subheader("Revenue by Product")

product_revenue = (
    filtered_df.groupby('product')['total_sar']
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(product_revenue)

# Additional information
st.subheader("Sales Data")
st.dataframe(filtered_df, use_container_width=True)

st.caption("Qahwa Corner | Cloud Computing for Data Science")
