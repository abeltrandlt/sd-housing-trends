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
- [Zillow Research Data](https://www.zillow.com/research/data/)  (planned extension)
  - Zillow Home Value Index (ZHVI)  
  - Median Sale Prices  

## Tools
- **SQL**: For structured queries (SQLite/PostgreSQL).
- **Python**: Data cleaning, EDA, and time-series analysis (`pandas`, `matplotlib`, `seaborn`, `statsmodels`).
- **Tableau Public**: For dashboards and interactive visualizations.
- **GitHub**: For project version control and documentation.

## Project Workflow
1. **Data Collection**: Download datasets from Redfin and Zillow.
          The raw Redfin data was downloaded in `.tsv000` format and required basic cleaning:
          - Parsed as tab-separated values using `pandas.read_csv(sep='\t')`
          - Filtered to San Diego metro region (`PARENT_METRO_REGION == 'San Diego, CA'`)
          - Selected and renamed relevant columns:
            - `PERIOD_BEGIN` → `date`
            - `MEDIAN_SALE_PRICE` → `median_price`
            - `INVENTORY` → `inventory`
            - `HOMES_SOLD` → `homes_sold`
          - Converted `date` to datetime format
          - Sorted chronologically
          - Saved to `data/processed/san_diego_housing_metrics.csv`
          - 
          > The cleaned dataset includes 1,458 monthly records from Redfin for the San Diego housing market and serves as the foundation for further analysis.
   
2. **Database Setup**: Design SQL schema and load data into tables (`date`, `median_price`, `inventory`, `homes_sold`) via Python.
          Schema made simple by design to support initial EDA & time series analysis.
          Script: load_to_postgres.py

4. **Exploratory Data Analysis (EDA)**: Use Python for trend plots, correlations, and descriptive stats.
     Note: The cleaned CSV file `san_diego_housing_metrics.csv` exceeds GitHub's file size limit. It is available locally or upon request.
5. **Time-Series Analysis**: Explore seasonal trends and rolling averages.  
6. **Visualization**: Build Tableau dashboards and link them here.  
7. **Documentation**: Record methodology and key insights in this repo.

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
