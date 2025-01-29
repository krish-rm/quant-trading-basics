# volatility_models.py
# Volatility models for options. This script implements volatility models including historical volatility and the GARCH (Generalized Autoregressive Conditional Heteroskedasticity) model.

import numpy as np
import pandas as pd
from arch import arch_model

def historical_volatility(data, window=20):
    """
    Calculate historical volatility as the rolling standard deviation of log returns.

    Args:
    data (pd.Series): Asset price data.
    window (int): The window size for calculating rolling volatility.

    Returns:
    pd.Series: Historical volatility
    """
    log_returns = np.log(data / data.shift(1))
    volatility = log_returns.rolling(window).std() * np.sqrt(252)  # Annualized volatility
    return volatility

def garch_volatility(data, p=1, q=1):
    """
    Estimate volatility using the GARCH model.

    Args:
    data (pd.Series): Asset returns data.
    p (int): Number of lag terms for the ARCH model.
    q (int): Number of lag terms for the GARCH model.

    Returns:
    pd.Series: GARCH model volatility
    """
    returns = np.log(data / data.shift(1)).dropna()
    model = arch_model(returns, vol='Garch', p=p, q=q)
    garch_result = model.fit(disp="off")
    return garch_result.conditional_volatility

# Example usage:
# hist_volatility = historical_volatility(stock_data['price'])
# garch_volatility = garch_volatility(stock_data['price'])
