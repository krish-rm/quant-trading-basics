# backtesting.py

import numpy as np
import pandas as pd

def backtest_strategy(data, signals, initial_capital=10000):
    """
    Backtest an equity strategy based on buy/sell signals.

    Args:
    data (pd.DataFrame): Data with prices.
    signals (np.ndarray): Array of signals (1 for buy, -1 for sell, 0 for hold).
    initial_capital (float): Starting capital for the backtest.

    Returns:
    float: Final portfolio value after backtesting.
    """
    capital = initial_capital
    position = 0
    portfolio_values = []

    # Loop through the data and apply the signals
    for i in range(1, len(data)):
        # Buy signal (enter position)
        if signals[i] == 1 and capital > 0:
            position = capital / data['price'][i]  # Buy the asset
            capital = 0  # Use all capital for buying

        # Sell signal (exit position)
        elif signals[i] == -1 and position > 0:
            capital = position * data['price'][i]  # Sell the asset and convert to cash
            position = 0  # Exit the position

        # Calculate the current portfolio value
        portfolio_value = capital + position * data['price'][i]
        portfolio_values.append(portfolio_value)

    final_portfolio_value = portfolio_values[-1] if portfolio_values else capital
    return final_portfolio_value

# Example usage:
# final_value = backtest_strategy(stock_data, signals)
