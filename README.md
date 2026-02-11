# sd-housing-trends
# San Diego Housing Market Analysis

## Overview
Analyzed Redfin housing data to explore pricing trends, inventory changes, and market dynamics in San Diego. Built an interactive Tableau dashboard with EDA insights and visualizations.

## Objectives
- **Understand San Diego housing price trends** (5-year focus).
- **Analyze correlation between supply and price** over time.
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
- **GitHub, VSCode**: For project version control and documentation.

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
+── data/ # Raw and cleaned datasets
│   +── raw/ # Raw downloads (Redfin/Zillow CSVs)
│   +── processed/ # Cleaned CSV files ready for analysis
+── notebooks/ # Jupyter notebooks for analysis (EDA, modeling)
+── sql/ # SQL scripts for schema and queries
+── visuals/ # Exported plots for GitHub preview
+── tableau/ # Tableau workbook (.twbx) and dashboard links
+── README.md # Project overview (this file)
+── requirements.txt # Python dependencies (to recreate environment)

## Tableau Dashboard
- Median price trends + 3-month rolling average
- Price vs Inventory (dual axis)
- YoY metric changes (bar chart)
*https://public.tableau.com/app/profile/alberto.beltran.de.la.torre/viz/Book1_17557936058330/Dashboard1*

## Key Takeaways
1. **Price Peak**: Median prices peaked in May 2022 after a 45% increase from April 2020.
2. **Demand Cooling**: YoY declines in homes sold, inventory, and list-to-sale ratio in 2023.
3. **Supply-Driven Pricing**: Strong inverse correlation (r = -0.79) between inventory and prices.

## Next Steps
- [ ] Expand to include Zillow datasets
- [ ] Automate monthly market updates
 
