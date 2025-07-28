# sd-housing-trends
# San Diego Housing Trends Analysis

## Overview
This project analyzes the San Diego housing market using historical data from Redfin and Zillow. It examines price trends, inventory changes, and market dynamics over time, culminating in an interactive Tableau dashboard.

## Objectives
- **Understand housing price trends** (5-year view, zip code focus).
- **Analyze inventory and sales volume changes** over time.
- **Identify key patterns or anomalies** (e.g., COVID spikes).
- **Visualize findings** using Tableau for interactive insights.

## Data Sources
- [Redfin Data Center](https://www.redfin.com/news/data-center/)  
  - `monthly-median-sale-price`  
  - `monthly-housing-inventory`  
  - `monthly-home-sales`  
- [Zillow Research Data](https://www.zillow.com/research/data/)  
  - Zillow Home Value Index (ZHVI)  
  - Median Sale Prices  

## Tools
- **SQL**: For structured queries (SQLite/PostgreSQL).
- **Python**: Data cleaning, EDA, and time-series analysis (`pandas`, `matplotlib`, `seaborn`, `statsmodels`).
- **Tableau Public**: For dashboards and interactive visualizations.
- **GitHub**: For project version control and documentation.

## Project Workflow
1. **Data Collection**: Download datasets from Redfin and Zillow.  
2. **Database Setup**: Design SQL schema and load data into tables (`prices`, `inventory`, `sales`).  
3. **Exploratory Data Analysis (EDA)**: Use Python for trend plots, correlations, and descriptive stats.  
4. **Time-Series Analysis**: Explore seasonal trends and rolling averages.  
5. **Visualization**: Build Tableau dashboards and link them here.  
6. **Documentation**: Record methodology and key insights in this repo.

## Repository Structure
├── data/ # Raw and cleaned datasets
│ ├── raw/ # Raw downloads (Redfin/Zillow CSVs)
│ └── processed/ # Cleaned CSV files ready for analysis
├── notebooks/ # Jupyter notebooks for analysis (EDA, modeling)
├── sql/ # SQL scripts for schema and queries
├── visuals/ # Exported plots for GitHub preview
├── tableau/ # Tableau workbook (.twbx) and dashboard links
├── README.md # Project overview (this file)
└── requirements.txt # Python dependencies (to recreate environment)


## Next Steps
- [ ] Populate the `data/raw/` folder with downloaded Redfin and Zillow data.  
- [ ] Define the SQL schema (`sql/schema.sql`) for `prices`, `sales`, and `inventory`.  
- [ ] Begin Python EDA in `notebooks/eda.ipynb`.  

## Tableau Dashboard
*(Link will be added after dashboard creation.)*
