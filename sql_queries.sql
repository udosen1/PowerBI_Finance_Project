USE FinancePortfolioDB;

-- Create the table for the large, combined historical market data
CREATE TABLE MarketData (
	[Date] DATE,
	[Open] DECIMAL(18, 4), 
	[High] DECIMAL(18, 4),
	[Low] DECIMAL(18, 4),
	[Close] DECIMAL(18, 4),
	[Volume] BIGINT, 
    [OpenInt] INT,
	[Ticker] VARCHAR(10)
); 

-- Create the table for your small, personal portfolio holdings
CREATE TABLE PortfolioHoldings (
    Ticker VARCHAR(10),
    PurchaseDate DATE,
    PurchasePrice DECIMAL(18, 4),
    Quantity INT,
    Sector VARCHAR(50)
);

-- Load data into the MarketData table
BULK INSERT MarketData
FROM 'C:\Users\ASUS\Documents\PowerBI_Finance_Project\combined_market_data.csv'
WITH (
    FIELDTERMINATOR = ',',  -- CSV files are comma-separated
    ROWTERMINATOR = '\n',   -- Each row ends with a new line
    FIRSTROW = 2            -- IMPORTANT: This skips the header row in your CSV
);

-- Load data into the PortfolioHoldings table
BULK INSERT PortfolioHoldings
FROM 'C:\Users\ASUS\Documents\PowerBI_Finance_Project\portfolio_holdings.csv' 
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

-- Check the row counts to ensure data was loaded
SELECT 'MarketData' as TableName, COUNT(*) as NumberOfRows FROM MarketData
UNION ALL
SELECT 'PortfolioHoldings' as TableName, COUNT(*) as NumberOfRows FROM PortfolioHoldings;
GO