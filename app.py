
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Interactive Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interactive Sales Dashboard")
st.write("Analyze sales, profit and regional performance.")

# Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May",
              "Jun", "Jul", "Aug", "Sep", "Oct"],
    "Sales": [12000, 15000, 18000, 14000, 20000,
              22000, 19000, 25000, 28000, 30000],
    "Profit": [3000, 4000, 5000, 3500, 6000,
               7000, 5500, 8000, 9000, 10000],
    "Region": ["North", "South", "East", "West", "North",
               "South", "East", "West", "North", "South"]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Dashboard Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

filtered_df = df[df["Region"].isin(regions)]

# KPI metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{filtered_df['Sales'].sum():,}")
col2.metric("Total Profit", f"₹{filtered_df['Profit'].sum():,}")
col3.metric("Average Sales", f"₹{filtered_df['Sales'].mean():,.0f}")

# Sales chart
st.subheader("Monthly Sales Analysis")

fig1 = px.bar(
    filtered_df,
    x="Month",
    y="Sales",
    color="Region",
    title="Sales by Month"
)

st.plotly_chart(fig1, use_container_width=True)

# Profit chart
st.subheader("Profit Analysis")

fig2 = px.line(
    filtered_df,
    x="Month",
    y="Profit",
    color="Region",
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)

# Data table
st.subheader("Sales Data")
st.dataframe(filtered_df, use_container_width=True)
