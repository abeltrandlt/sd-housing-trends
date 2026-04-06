# San Diego Housing Market Analysis  
**Supply, Demand, and Price Dynamics (2012–2025)**

---

## Overview
This project analyzes housing market dynamics in San Diego using Redfin data, focusing on the relationship between **inventory (supply), transaction activity (demand), and pricing behavior**.

The goal was not just to visualize trends, but to identify **what actually drives price movement** and how market conditions shifted during and after COVID.

---

## Key Questions
- What drove the rapid price acceleration from 2020 to 2022?
- How strongly does inventory influence price behavior?
- Did demand meaningfully contract in 2023?
- Are there leading indicators that precede price movement?

---

## Dataset
- **Source**: Redfin Data Center  
- **Scope**: San Diego Metro Area  
- **Time Range**: 2012 – 2025  
- **Granularity**: Monthly  
- **Records**: 1,458 observations  

### Core Features
- Median Sale Price  
- Inventory  
- Homes Sold  
- Pending Sales  
- New Listings  
- Days on Market  
- Sale-to-List Ratio  

---

## Tools & Stack
- **Python (Pandas, Seaborn, Matplotlib)** → EDA & feature engineering  
- **SQL (PostgreSQL)** → Data storage & querying  
- **Tableau** → Business-facing visualization  
- **GitHub** → Version control & documentation  

---

## Methodology

### 1. Data Processing
- Filtered to the San Diego metro region
- Aggregated to monthly averages
- Engineered features:
  - 3-month rolling averages
  - MoM and YoY % changes
  - Lagged relationships (inventory → future price)

### 2. Exploratory Analysis
- Time-series trend analysis (price, inventory, sales)
- Rolling average smoothing
- Demand contraction analysis (2023)
- Correlation + lag analysis

### 3. Visualization
- Built a Tableau dashboard for:
  - Price trend + moving average
  - Price vs inventory (dual axis)
  - YoY demand shifts

---

## Key Insights

### 1. Price Acceleration Was Supply-Driven
- Median price increased ~45.8% (Apr 2020 → May 2022)  
- Inventory fell ~34% over the same period  

**Interpretation:**  
Price growth aligned directly with supply contraction.

---

### 2. Inventory Leads Price (Short-Term Signal)
- Strongest inverse correlations occurred at 1–5 month lags (~ -0.25)  

**Interpretation:**  
Inventory tightening tends to **precede upward price pressure**, making it a usable short-term signal.

---

### 3. 2023 Marked a Clear Demand Reset
- Homes Sold: -22.3% YoY  
- Pending Sales: -18.5% YoY  
- New Listings: -21.9% YoY  

**Interpretation:**  
Demand contraction was broad—not isolated—likely driven by affordability and rising rates.

---

### 4. Inventory is the Dominant Price Driver
- Correlation with price: -0.79  

**Interpretation:**  
Supply constraints are the primary lever in this market.  
Transaction volume reflects the market—it doesn’t drive it.

---

## Tableau Dashboard
🔗 *(https://public.tableau.com/app/profile/alberto.beltran.de.la.torre/viz/Book1_17557936058330/Dashboard1)*  

### Views Included
- Median Price + 3-Month Moving Average  
- Price vs Inventory (dual axis)  
- YoY Demand Changes (2023)  

---

## Repository Structure

data/
raw/
processed/
notebooks/
sql/
tableau/
README.md

---

## What This Project Demonstrates
- Time-series analysis & feature engineering  
- Translating raw data → business insight  
- Identifying leading vs lagging indicators  
- Communicating findings clearly (technical → non-technical)  

---

## Next Steps (Extensions)
- Integrate Zillow Home Value Index (ZHVI)  
- Build a short-term price forecasting model  
- Automate monthly market updates  

---
