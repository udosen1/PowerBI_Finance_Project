# Project: Risk-Return Navigator - A Power BI Portfolio Analysis

## Project Description

This project is a data analytics portfolio piece designed to showcase skills in data preparation, database management, and business intelligence. The goal is to build a "Risk-Return Navigator," an interactive Power BI dashboard that analyzes the performance and risk profile of a hypothetical investment portfolio. The project leverages Python for data wrangling, SQL for data storage and querying, and Power BI for creating compelling, data-driven visualizations.

**Key Skills Demonstrated:**
*   Data Cleaning and Aggregation (Python)
*   Database Design and Management (SQL)
*   Data Modeling and DAX Calculations (Power BI)
*   Interactive Dashboard Design (Power BI)
*   Financial Metrics Analysis (Risk, Return, Benchmarking)

---

## Data Source

The historical price and volume data for all US stocks and ETFs is sourced from the following Kaggle dataset:
*   **Link:** [Price-Volume-Data-For-All-US-Stocks-ETFs](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)

---

## Setup and Usage Guide

Follow these steps to set up the project environment and prepare the data for analysis.

### 1. Prerequisites

Ensure you have the following tools installed:
*   Python 3.x
*   Pandas library for Python (`pip install pandas`)
*   A SQL Server instance (e.g., Microsoft SQL Server Express)
*   A database management tool (e.g., SSMS)
*   Power BI Desktop

### 2. Required File Structure

For the data preparation script to work correctly, your project folder must be organized as follows:

```
/PowerBI_Finance_Project/
    |
    |-- combine_data.py       <-- The Python script provided
    |
    |-- Stocks/               <-- Folder containing all .us.txt stock files from Kaggle
    |   |-- aapl.us.txt
    |   |-- msft.us.txt
    |   |-- ... etc.
    |
    |-- ETFs/                 <-- Folder containing all .us.txt ETF files from Kaggle
        |-- spy.us.txt
        |-- qqq.us.txt
        |-- ... etc.
```

### 3. Data Preparation Steps

**Step A: Combine Raw Data Files**
Run the `combine_data.py` script from your terminal within the root of the project folder:
```bash
python combine_data.py
```
This script will process the selected ticker files from the `Stocks` and `ETFs` folders and generate a single, clean master file named **`combined_market_data.csv`**.

**Step B: Create Portfolio Holdings File**
Create a new file named **`portfolio_holdings.csv`**. This file defines your hypothetical portfolio. Add your chosen assets with the following structure:
```csv
Ticker,PurchaseDate,PurchasePrice,Quantity,Sector
AAPL,2017-01-03,116.15,50,Technology
MSFT,2017-01-03,62.58,60,Technology
JPM,2017-02-01,87.31,70,Financials
GLD,2017-04-03,120.00,30,Commodity
```

### 4. Database and Power BI Workflow

**Step C: Set up SQL Database**
In your SQL Server, create two tables to hold the project data. Use the following SQL schemas:
```sql
-- 1. For the combined historical market data
CREATE TABLE MarketData (
    [Date] DATE,
    [Open] DECIMAL(18, 4),
    [High] DECIMAL(18, 4),
    [Low] DECIMAL(18, 4),
    [Close] DECIMAL(18, 4),
    [Volume] BIGINT,
    [Ticker] VARCHAR(10)
);

-- 2. For your hypothetical portfolio holdings
CREATE TABLE PortfolioHoldings (
    Ticker VARCHAR(10),
    PurchaseDate DATE,
    PurchasePrice DECIMAL(18, 4),
    Quantity INT,
    Sector VARCHAR(50)
);
```

**Step D: Import Data into SQL**
Use your database tool (like SSMS) to import the data from:
1.  `combined_market_data.csv` -> into the `MarketData` table.
2.  `portfolio_holdings.csv` -> into the `PortfolioHoldings` table.

**Step E: Connect Power BI**
You are now ready to begin the analysis:
1.  Open Power BI Desktop.
2.  Select "Get Data" > "SQL Server".
3.  Connect to your database.
4.  Load the `MarketData` and `PortfolioHoldings` tables.
5.  Begin building your data model, DAX measures, and dashboard visualizations.


# Project: Risk-Return Navigator - A Power BI Portfolio Analysis

## 🚀 Live Interactive Dashboard

The full, interactive Power BI report is publicly available for you to explore. No software is required.

**[➡️ Click Here to View the Live Interactive Dashboard](https://your-public-power-bi-url-here)** 

---

## 📊 Dashboard Showcase

Here is a preview of the three main pages of the report.

### Page 1: Portfolio Overview (The Executive Summary)
*This page provides a high-level, at-a-glance summary of the portfolio's health, tracking key performance indicators and comparing performance against the S&P 500 benchmark.*

![Portfolio Overview Screenshot](https://github.com/udosen1/PowerBI_Finance_Project/blob/main/Portfolio_Overview.png)

### Page 2: Performance Deep Dive (The "Why")
*This page allows for a deeper analysis of what drives the portfolio's returns, breaking down profit and loss by individual assets and by sector.*

![Performance Deep Dive Screenshot](https://github.com/udosen1/PowerBI_Finance_Project/blob/main/Performance_Deep_Dive.png)

### Page 3: Risk Analysis (The "How Risky")
*This page visualizes the crucial tradeoff between risk (volatility) and return, allowing for a sophisticated analysis of the portfolio's risk profile.*

![Risk Analysis Screenshot](https://github.com/udosen1/PowerBI_Finance_Project/blob/main/Risk_Analysis.png)

---

## 🎯 Project Objective

The goal of this project was to develop an end-to-end business intelligence solution to address the challenge of tracking investment portfolio performance. The "Risk-Return Navigator" dashboard transforms raw, historical market data into an interactive tool for making informed financial decisions.

---

## 🛠️ Technology Stack

*   **Data Preparation:** **Python (Pandas)** for cleaning, processing, and combining raw data files.
*   **Data Storage:** **Microsoft SQL Server** for storing over 100,000 records of market data.
*   **Business Intelligence:** **Power BI** for data modeling, advanced DAX calculations, and interactive visualization.

---

## ⚙️ Data Pipeline & Architecture

1.  **Data Sourcing:** Historical price data for 21 securities was sourced from a public Kaggle dataset.
2.  **Data Preparation:** A Python script automated the aggregation of the raw files into a single, clean dataset.
3.  **Database Loading:** The processed data was efficiently loaded into a SQL Server database using `BULK INSERT`.
4.  **Data Modeling:** A **Star Schema** was implemented in Power BI, with a central `Fact_MarketData` table connected to `Dim_Date` and `Dim_Security` dimensions. This best-practice model ensures high performance and enables powerful time-intelligence analysis.

---

## 💡 Key Insights Generated

*   **Performance vs. Benchmark:** The portfolio successfully outperformed its S&P 500 benchmark, driven primarily by strong performance in the Technology sector.
*   **Risk-Return Profile:** The scatter plot identified key assets like TSLA as high-return but high-volatility, while assets like Johnson & Johnson acted as stabilizing, low-risk forces.
*   **Actionable Strategy:** The dashboard revealed that the portfolio is heavily weighted towards Technology. A potential action would be to rebalance by investing more in under-represented, low-volatility sectors to mitigate risk.
