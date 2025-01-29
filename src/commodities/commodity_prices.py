# commodity_prices.py
# Data processing for commodities. This script is used to process commodity price data. It cleans the data, calculates daily returns, and prepares it for further analysis.

import pandas as pd
import numpy as np

def load_commodity_data(file_path):
    """
    Load commodity price data from a CSV file.

    Args:
    file_path (str): Path to the CSV file containing commodity prices.

    Returns:
    pd.DataFrame: A DataFrame containing the commodity price data.
    """
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    return data

def calculate_daily_returns(data):
    """
    Calculate the daily returns of the commodity prices.

    Args:
    data (pd.DataFrame): A DataFrame containing commodity prices.

    Returns:
    pd.DataFrame: A DataFrame with daily returns.
    """
    data['Daily Return'] = data['Price'].pct_change()
    data.dropna(inplace=True)
    return data

def plot_commodity_prices(data):
    """
    Plot the commodity prices over time.

    Args:
    data (pd.DataFrame): A DataFrame containing commodity prices.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Price'], label='Commodity Price')
    plt.title('Commodity Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Example usage:
# data = load_commodity_data('commodity_data.csv')
# data = calculate_daily_returns(data)
# plot_commodity_prices(data)
