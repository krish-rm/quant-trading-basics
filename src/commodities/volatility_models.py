# volatility_models.py
# Volatility models for commodities. This script demonstrates a basic volatility model for commodities, using GARCH(1, 1) to model the time-varying volatility.

import pandas as pd
import numpy as np
from arch import arch_model

def estimate_volatility(data):
    """
    Estimate the volatility of commodity returns using a GARCH(1, 1) model.

    Args:
    data (pd.DataFrame): A DataFrame containing commodity returns.

    Returns:
    pd.Series: A series with the estimated volatility over time.
    """
    # Fit a GARCH(1, 1) model
    model = arch_model(data['Daily Return'], vol='Garch', p=1, q=1)
    results = model.fit(disp="off")
    
    # Get the conditional volatility
    volatility = results.conditional_volatility
    return volatility

def plot_volatility(volatility):
    """
    Plot the estimated volatility over time.

    Args:
    volatility (pd.Series): A series with estimated volatility.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(volatility, label='Estimated Volatility')
    plt.title('Commodity Volatility Over Time (GARCH Model)')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.legend()
    plt.show()

# Example usage:
# data = load_commodity_data('commodity_data.csv')
# data = calculate_daily_returns(data)
# volatility = estimate_volatility(data)
# plot_volatility(volatility)
