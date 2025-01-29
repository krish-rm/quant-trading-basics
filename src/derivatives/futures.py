# futures.py
# Futures pricing and trading logic. This script implements futures pricing based on the cost-of-carry model and a simple futures trading strategy.

import numpy as np

def futures_price(S, r, T, cost_of_carry=0):
    """
    Futures pricing model using the cost-of-carry model.

    Args:
    S (float): Spot price of the underlying asset
    r (float): Risk-free interest rate
    T (float): Time to maturity (in years)
    cost_of_carry (float): Cost of carry (storage, insurance, etc.)

    Returns:
    float: The futures price
    """
    futures_price = S * np.exp((r + cost_of_carry) * T)
    return futures_price

def futures_trading_strategy(data, initial_capital=10000):
    """
    A simple futures trading strategy based on momentum.

    Args:
    data (pd.Series): Series of futures prices.
    initial_capital (float): Starting capital for the strategy.

    Returns:
    float: Final portfolio value after trading.
    """
    capital = initial_capital
    position = 0
    portfolio_values = []

    # Loop through the data and simulate trading
    for i in range(1, len(data)):
        # Buy signal: If the price has increased compared to the previous period
        if data[i] > data[i-1]:
            if capital > 0:  # Enter a long position
                position = capital / data[i]
                capital = 0
        # Sell signal: If the price has decreased compared to the previous period
        elif data[i] < data[i-1]:
            if position > 0:  # Exit the long position
                capital = position * data[i]
                position = 0

        # Track portfolio value
        portfolio_value = capital + position * data[i]
        portfolio_values.append(portfolio_value)

    final_value = portfolio_values[-1] if portfolio_values else capital
    return final_value

# Example usage:
# futures_price_value = futures_price(100, 0.05, 0.5)
# final_portfolio_value = futures_trading_strategy(futures_data)
