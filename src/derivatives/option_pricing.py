# option_pricing.py
# Option pricing models: Black-Scholes, Binomial tree. This script implements option pricing using the Black-Scholes model and the Binomial Tree model.

import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    """
    Black-Scholes option pricing model for European options.

    Args:
    S (float): Spot price of the asset
    K (float): Strike price
    T (float): Time to maturity (in years)
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying asset
    option_type (str): Type of option ('call' or 'put')

    Returns:
    float: The theoretical price of the option
    """
    # Calculate d1 and d2
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # Call option pricing formula
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    # Put option pricing formula
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'")

    return price

def binomial_tree_price(S, K, T, r, sigma, n=100, option_type='call'):
    """
    Binomial Tree option pricing model for European options.

    Args:
    S (float): Spot price of the asset
    K (float): Strike price
    T (float): Time to maturity (in years)
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying asset
    n (int): Number of steps in the binomial tree
    option_type (str): Type of option ('call' or 'put')

    Returns:
    float: The theoretical price of the option
    """
    # Calculate the parameters of the binomial model
    dt = T / n  # Time step
    u = np.exp(sigma * np.sqrt(dt))  # Up factor
    d = 1 / u  # Down factor
    q = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral probability

    # Initialize asset prices at maturity
    prices = np.array([S * u ** j * d ** (n - j) for j in range(n + 1)])

    # Calculate option values at maturity
    if option_type == 'call':
        values = np.maximum(prices - K, 0)
    elif option_type == 'put':
        values = np.maximum(K - prices, 0)
    else:
        raise ValueError("Option type must be 'call' or 'put'")

    # Step backward through the binomial tree
    for i in range(n - 1, -1, -1):
        values = np.exp(-r * dt) * (q * values[1:i+2] + (1 - q) * values[:i+1])

    return values[0]

# Example usage:
# bs_price = black_scholes_price(100, 95, 1, 0.05, 0.2, 'call')
# binomial_price = binomial_tree_price(100, 95, 1, 0.05, 0.2, 100, 'call')
