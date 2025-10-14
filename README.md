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


## 📊 Dashboard Showcase

Here is a preview of the three main pages of the report.

### Page 1: Portfolio Overview (The Executive Summary)
*This page provides a high-level, at-a-glance summary of the portfolio's health, tracking key performance indicators and comparing performance against the S&P 500 benchmark.*

![Portfolio Overview Screenshot](https://github.com/udosen1/PowerBI_Finance_Project/blob/main/Portfolio_overview.png)
