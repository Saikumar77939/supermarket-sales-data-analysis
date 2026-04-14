import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from prophet import Prophet
from datetime import datetime

# Load Data
@st.cache_data
def load_data():
    df = pd.read_excel("D:\\today\\ANALYSIS ON SUPERMARKETSALES.xlsx")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
city = st.sidebar.multiselect("Select City", options=df["City"].unique(), default=df["City"].unique())
gender = st.sidebar.multiselect("Select Gender", options=df["Gender"].unique(), default=df["Gender"].unique())

df_filtered = df[(df["City"].isin(city)) & (df["Gender"].isin(gender))]

# Title
st.title("Supermarket Sales Dashboard")

# KPIs
total_sales = df_filtered["Total"].sum()
avg_rating = np.round(df_filtered["Rating"].mean(), 2)
avg_tax = df_filtered["Tax 5%"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Avg. Rating", f"{avg_rating}")
col3.metric("Avg. Tax", f"${avg_tax:.2f}")

# Sales by Product Line
st.subheader("Sales by Product Line")
sales_by_product = df_filtered.groupby("Product line")["Total"].sum().sort_values()
fig_product = px.bar(sales_by_product, orientation='h', color=sales_by_product.values, color_continuous_scale="Agsunset", labels={"value": "Total Sales", "index": "Product Line"})
st.plotly_chart(fig_product, use_container_width=True)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")
monthly_sales = df_filtered.groupby("Month")["Total"].sum().reset_index()
monthly_sales["Month"] = monthly_sales["Month"].astype(str)
fig_month = px.line(monthly_sales, x="Month", y="Total", markers=True, title="Monthly Sales")
st.plotly_chart(fig_month, use_container_width=True)

# Gender Distribution
st.subheader("Gender Distribution")
fig_gender = px.pie(df_filtered, names='Gender', title='Customer Gender Distribution', hole=0.5)
st.plotly_chart(fig_gender, use_container_width=True)

# Forecasting with Prophet
st.subheader("Sales Forecasting (Prophet)")
sales_by_date = df_filtered.groupby('Date')['Total'].sum().reset_index()
sales_by_date.columns = ['ds', 'y']

model = Prophet()
model.fit(sales_by_date)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

fig_forecast = px.line(forecast, x='ds', y='yhat', title='Sales Forecast for Next 30 Days')
st.plotly_chart(fig_forecast, use_container_width=True)

# Customer Segmentation
st.subheader("Customer Segmentation (KMeans)")
cust_df = df_filtered.groupby('Customer type')[['Total']].mean()
cust_df_scaled = (cust_df - cust_df.mean()) / cust_df.std()

kmeans = KMeans(n_clusters=2, random_state=42)
cust_df['Cluster'] = kmeans.fit_predict(cust_df_scaled)

fig_cluster = px.bar(cust_df, x=cust_df.index, y='Total', color=cust_df['Cluster'].astype(str), title='Customer Segments')
st.plotly_chart(fig_cluster, use_container_width=True)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
numeric_df = df_filtered.select_dtypes(include=[np.number])
fig_corr = px.imshow(numeric_df.corr(), color_continuous_scale='RdBu_r', title='Correlation Matrix')
st.plotly_chart(fig_corr, use_container_width=True)

st.success("Dashboard Loaded Successfully")

