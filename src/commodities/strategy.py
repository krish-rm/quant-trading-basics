# strategy.py
# Strategies for commodity trading. This script outlines a simple commodity trading strategy based on moving averages, where a long position is taken when the short-term moving average crosses above the long-term moving average.

import pandas as pd
import numpy as np

def moving_average_strategy(data, short_window=50, long_window=200):
    """
    Implement a moving average crossover strategy for commodity trading.

    Args:
    data (pd.DataFrame): A DataFrame containing commodity prices.
    short_window (int): The window for the short-term moving average (default 50).
    long_window (int): The window for the long-term moving average (default 200).

    Returns:
    pd.DataFrame: A DataFrame with signals to buy or sell.
    """
    data['Short MA'] = data['Price'].rolling(window=short_window).mean()
    data['Long MA'] = data['Price'].rolling(window=long_window).mean()

    data['Signal'] = 0
    data['Signal'][short_window:] = np.where(data['Short MA'][short_window:] > data['Long MA'][short_window:], 1, 0)
    data['Position'] = data['Signal'].diff()

    return data

def backtest_strategy(data, initial_capital=10000):
    """
    Backtest the moving average strategy on commodity data.

    Args:
    data (pd.DataFrame): A DataFrame with commodity prices and trading signals.
    initial_capital (float): The initial amount of capital for trading.

    Returns:
    pd.DataFrame: A DataFrame showing the portfolio value over time.
    """
    data['Daily Return'] = data['Price'].pct_change()
    data['Portfolio Value'] = initial_capital * (1 + data['Position'].shift(1) * data['Daily Return']).cumprod()

    return data

# Example usage:
# data = load_commodity_data('commodity_data.csv')
# data = moving_average_strategy(data)
# backtested_data = backtest_strategy(data)
