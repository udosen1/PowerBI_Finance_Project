import pandas as pd
import os

def combine_market_data():
    """
    Combines historical data for selected stocks and ETFs into a single CSV file.

    This script reads individual ticker files from 'Stocks' and 'ETFs' subfolders,
    adds a 'Ticker' column to identify the security, and merges them all into
    a master file named 'combined_market_data.csv'.
    """
    
    # --- Configuration ---
    # Define the tickers for the stocks and ETFs you have selected.
    # The script will look for files like 'aapl.us.txt', 'spy.us.txt', etc.
    stock_tickers = [
        'aapl.us.txt', 'aav.us.txt', 'ait.us.txt', 'jnj.us.txt', 'jpm.us.txt',
        'msft.us.txt', 'ncs.us.txt', 'pg.us.txt', 'rt.us.txt', 'tcbk.us.txt',
        'tex.us.txt', 'thm.us.txt', 'toca.us.txt', 'tsla.us.txt', 'xom.us.txt'
    ]
    
    etf_tickers = [
        'aadr.us.txt', 'agf.us.txt', 'agnd.us.txt', 'gld.us.txt', 'qqq.us.txt', 
        'spy.us.txt'
    ]

    # Define the subfolder names
    stocks_folder = 'Stocks'
    etfs_folder = 'ETFs'
    
    # List to hold all the individual dataframes
    all_data = []

    print("Starting data combination process...")

    # --- Process Stocks ---
    print(f"\nProcessing files from '{stocks_folder}' folder...")
    for ticker_file in stock_tickers:
        file_path = os.path.join(stocks_folder, ticker_file)
        if os.path.exists(file_path):
            try:
                # Read the CSV file
                df = pd.read_csv(file_path)
                # Extract the ticker symbol from the filename (e.g., 'aapl.us.txt' -> 'AAPL')
                ticker_symbol = ticker_file.split('.')[0].upper()
                # Add the ticker symbol as a new column
                df['Ticker'] = ticker_symbol
                all_data.append(df)
                print(f"  Successfully processed: {ticker_file}")
            except Exception as e:
                print(f"  Could not process {ticker_file}. Error: {e}")
        else:
            print(f"  File not found, skipping: {file_path}")

    # --- Process ETFs ---
    print(f"\nProcessing files from '{etfs_folder}' folder...")
    for ticker_file in etf_tickers:
        file_path = os.path.join(etfs_folder, ticker_file)
        if os.path.exists(file_path):
            try:
                # Read the CSV file
                df = pd.read_csv(file_path)
                # Extract the ticker symbol from the filename
                ticker_symbol = ticker_file.split('.')[0].upper()
                # Add the ticker symbol as a new column
                df['Ticker'] = ticker_symbol
                all_data.append(df)
                print(f"  Successfully processed: {ticker_file}")
            except Exception as e:
                print(f"  Could not process {ticker_file}. Error: {e}")
        else:
            print(f"  File not found, skipping: {file_path}")
            
    # --- Combine and Save ---
    if all_data:
        # Concatenate all dataframes in the list into a single dataframe
        master_dataframe = pd.concat(all_data, ignore_index=True)
        
        # Define the output filename
        output_filename = 'combined_market_data.csv'
        
        # Save the combined dataframe to a new CSV file
        master_dataframe.to_csv(output_filename, index=False)
        
        print(f"\n✅ Success! All data has been combined into '{output_filename}'.")
        print(f"   Total rows created: {len(master_dataframe)}")
    else:
        print("\n❌ No data was processed. Please check your folder structure and file names.")

if __name__ == "__main__":
    combine_market_data()