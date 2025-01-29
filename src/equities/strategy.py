# strategy.py
#  Equity strategy logic: Momentum and Mean Reversion. This script implements a simple momentum strategy where we buy when the price increases and sell when it decreases.


import numpy as np

def momentum_strategy(data, window_size=14):
    """
    Implements a simple momentum strategy based on the rate of change in price.

    Args:
    data (pd.Series): Price data or returns data for the stock.
    window_size (int): Number of periods to calculate momentum.

    Returns:
    np.ndarray: Signals array (1 for buy, -1 for sell, 0 for hold)
    """
    # Calculate momentum (change in price)
    momentum = data.diff(window_size)

    # Generate buy (1) or sell (-1) signals based on momentum
    signals = np.where(momentum > 0, 1, np.where(momentum < 0, -1, 0))
    
    return signals

def mean_reversion_strategy(data, window_size=20, threshold=0.02):
    """
    Implements a mean reversion strategy.

    Args:
    data (pd.Series): Stock price data.
    window_size (int): Rolling window size for moving average.
    threshold (float): Threshold for entering trades.

    Returns:
    np.ndarray: Signals array (1 for buy, -1 for sell, 0 for hold)
    """
    # Calculate rolling mean and standard deviation
    rolling_mean = data.rolling(window=window_size).mean()
    rolling_std = data.rolling(window=window_size).std()

    # Define the upper and lower bounds for mean reversion
    upper_bound = rolling_mean + rolling_std * threshold
    lower_bound = rolling_mean - rolling_std * threshold

    # Generate signals based on crossing the bounds
    signals = np.where(data > upper_bound, -1, np.where(data < lower_bound, 1, 0))
    
    return signals

# Example usage:
# signals_momentum = momentum_strategy(stock_data['price'])
# signals_reversion = mean_reversion_strategy(stock_data['price'])
