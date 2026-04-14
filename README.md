Supermarket Sales Dashboard
An interactive sales analytics dashboard built using Streamlit, Plotly, and Prophet, designed to analyze and visualize supermarket sales data. This project includes filtering, KPI metrics, product trends, customer segmentation, and future sales forecasting.

Features
City & gender-based filtering KPIs: Total Sales, Average Rating, Average Tax Sales by product line Monthly sales trend (time series) Gender distribution donut chart 30-day future sales forecasting using Prophet Customer segmentation using KMeans clustering Correlation heatmap of numerical features

Technologies & Libraries Used
Tool : Purpose Python 3.7+ : Programming language Streamlit : Build interactive web dashboard Pandas : Data loading and manipulation NumPy : Numerical computations Plotly Express : Interactive data visualizations Scikit-learn(KMeans) : Customer segmentation Prophet : Time-series forecasting OpenPyXL : Excel file reading support

Project Structure
graphql

supermarket-dashboard/ │ ├── dashboard.py # Streamlit app script ├── ANALYSIS ON SUPERMARKETSALES.xlsx # Dataset ├── requirements.txt # Python dependencies ├── README.md # Project documentation ├── .streamlit/ │ └── config.toml # Theme config for Streamlit Cloud (optional)

Installation & Setup (for Windows Command Prompt)
Clone the Repository cmd ---->git clone https://github.com/your-username/supermarket-dashboard.git cd supermarket-dashboard we can manually download the ZIP from GitHub and extract it.

Create a Virtual Environment cmd python -m venv venv venv\Scripts\activate You should see (venv) appear before your prompt.

Install Required Dependencies cmd ---->pip install -r requirements.txt If Prophet gives an error, try: c ---->pip install pystan==2.19.1.1 prophet

Add Your Dataset Excel file named: SUPERMARKET SALES ANALYSIS

ANALYSIS ON SUPERMARKETSALES.xlsx The project directory has been created, and the dashboard.py script is located within it. Make sure column names like Date, Total, and Gender match the ones used in this code.

Run the Streamlit App cmd streamlit run dashboard.py
default browser will automatically open at: --->http://localhost:8501 If it doesn't, just manually copy that URL into your browser.

Dashboard Sections Explained
Filters
Filter data by City and Gender via sidebar.

KPIs
Total Sales : Cumulative total of purchases. Avg. Rating : Average customer rating. Avg. Tax : Mean tax paid on purchases.

Visualizations
Sales by Product Line: Horizontal bar chart. Monthly Sales Trend: Time series line chart. Gender Distribution: Donut pie chart. Sales Forecast: Prophet-predicted 30-day sales trend. Customer Segmentation: KMeans clustering by customer type. Correlation Heatmap: Numerical relationship matrix.

requirements.txt
txt Copy Edit streamlit pandas numpy plotly openpyxl scikit-learn prophet

requirements.txt – Dependency Management
The requirements.txt file lists all the Python libraries that are required to run this project successfully. These libraries include core tools for building the dashboard, handling data, generating visualizations, and performing forecasting and clustering.

Each line in this file represents a package dependency that the Python interpreter will install using pip. This ensures that anyone who downloads your project can recreate the same development environment, avoiding compatibility issues.

Why It's Important: Environment Reproducibility : Keeps your app consistent across different systems. Quick Setup : One command installs everything in seconds. Easy Collaboration : Others (e.g., recruiters, teammates) can run your app without manual setup. Deployment Friendly : Required for deployment on platforms like Streamlit Cloud, Heroku, or Docker.

Installation Command: Once inside the project folder, the user just needs to run: bash

--->pip install -r requirements.txt

This command will automatically:
Install Streamlit for building the web app Install Pandas and NumPy for data analysis Install Plotly for visualizations Install Prophet and PyStan for time-series forecasting Install scikit-learn for clustering (KMeans) Install OpenPyXL to read Excel files

Contact
Developed by : Sai kumar Email : Pandirisaikumar779@gmail.com GitHub : https://github.com/Saikumar77939/supermarket-sales-data-analysis LinkedIn : www.linkedin.com/in/pandiri-sai-kumar
