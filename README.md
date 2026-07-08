# 📊 Bluestock Mutual Fund Analytics Capstone Project

## Overview

The **Bluestock Mutual Fund Analytics Capstone Project** is an end-to-end Data Analytics project developed as part of the **Bluestock Data Analytics Internship**.

The project focuses on analyzing mutual fund performance, investor behaviour, portfolio risk, and market trends using **Python, SQL, SQLite, and Power BI**. It demonstrates the complete data analytics lifecycle, including data ingestion, cleaning, analysis, visualization, and reporting.

---

# Project Objectives

- Develop an automated ETL pipeline.
- Clean and preprocess multiple mutual fund datasets.
- Store processed data in SQLite.
- Perform Exploratory Data Analysis (EDA).
- Calculate financial performance metrics.
- Perform advanced analytics.
- Build an interactive Power BI dashboard.
- Generate business insights for investment decision-making.

---

# Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Power BI
- Matplotlib
- Jupyter Notebook
- Git & GitHub

---

# Project Workflow

```
Raw CSV Files
      │
      ▼
ETL Pipeline
      │
      ▼
Data Cleaning
      │
      ▼
SQLite Database
      │
      ▼
Python Analytics
      │
      ▼
Power BI Dashboard
      │
      ▼
Business Insights
```

---

# Folder Structure

```
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│       └── bluestock_mf.db
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── README.md
└── requirements.txt
```

---

# Datasets Used

The project uses multiple datasets including:

- Fund Master
- NAV History
- Portfolio Holdings
- Investor Transactions
- Benchmark Indices
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count

---

# Project Modules

## 1. Data Ingestion

- Imported raw CSV files.
- Verified data integrity.
- Prepared datasets for preprocessing.

---

## 2. Data Cleaning

Performed:

- Duplicate removal
- Missing value treatment
- Date conversion
- Column standardization
- Data validation

---

## 3. Exploratory Data Analysis

Created visualizations for:

- NAV trends
- AUM growth
- Category distribution
- Investor behaviour
- Correlation analysis

---

## 4. Performance Analytics

Calculated:

- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Tracking Error
- Maximum Drawdown

Generated CSV reports for each metric.

---

## 5. Advanced Analytics

Implemented:

- Historical VaR (95%)
- Conditional VaR (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Rule-Based Fund Recommendation System
- Sector HHI Concentration Analysis

---

## 6. Power BI Dashboard

Designed a four-page interactive dashboard:

### Industry Overview

- KPI Cards
- AUM Trend
- Fund House Analysis

### Fund Performance

- Risk vs Return
- Benchmark Comparison
- Fund Scorecard

### Investor Analytics

- Investor Demographics
- Transaction Analysis
- SIP vs Lumpsum

### SIP & Market Trends

- SIP Growth
- NIFTY Comparison
- Category Inflows

Dashboard Features:

- Interactive Slicers
- Drill-through
- Tooltips
- Dynamic KPI Cards

---

# Key Insights

- Industry AUM showed continuous growth.
- SIP inflows increased steadily.
- Liquid funds demonstrated stable risk-adjusted returns.
- Small-cap funds generated higher returns with higher risk.
- Investor Cohort Analysis revealed changing investment patterns.
- SIP Continuity Analysis identified at-risk investors.
- Sector HHI measured portfolio diversification.

---

# Deliverables

- ETL Pipeline
- SQLite Database
- EDA Notebook
- Performance Analytics Notebook
- Advanced Analytics Notebook
- Interactive Power BI Dashboard
- Final Internship Report
- Presentation
- SQL Scripts
- CSV Reports

---

# Future Enhancements

- Live NAV API Integration
- Streamlit Web Application
- Monte Carlo Simulation
- Portfolio Optimization
- Automated Email Reports
- Cloud Deployment

---

# Author

**vprvithal**



Bluestock Fintech

---

# Acknowledgement

I sincerely thank **Bluestock Fintech** for providing the opportunity to work on this capstone project. This project helped strengthen my practical skills in Data Analytics, SQL, Python, SQLite, and Power BI while solving real-world financial analytics problems.
