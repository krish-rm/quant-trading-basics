# interest_rate_models.py
# Models for interest rate modeling. This script implements a simple interest rate model using the Cox-Ingersoll-Ross (CIR) model, which is a popular term structure model for interest rates.

import numpy as np
import matplotlib.pyplot as plt

def cir_model(r0, kappa, theta, sigma, T, dt=1/252, n_steps=252):
    """
    Simulate the evolution of interest rates using the Cox-Ingersoll-Ross (CIR) model.

    Args:
    r0 (float): Initial interest rate
    kappa (float): Rate of mean reversion
    theta (float): Long-term mean rate
    sigma (float): Volatility of interest rates
    T (float): Time to maturity (in years)
    dt (float): Time step size (default is 1/252, for daily steps)
    n_steps (int): Number of time steps (default is 252 for daily steps in 1 year)

    Returns:
    np.ndarray: Simulated interest rates over time
    """
    rates = np.zeros(n_steps)
    rates[0] = r0
    
    for t in range(1, n_steps):
        dr = kappa * (theta - rates[t-1]) * dt + sigma * np.sqrt(rates[t-1]) * np.sqrt(dt) * np.random.normal()
        rates[t] = rates[t-1] + dr
    
    return rates

def plot_interest_rate_paths(r0, kappa, theta, sigma, T, num_paths=5):
    """
    Plot multiple paths of simulated interest rates using the CIR model.

    Args:
    r0 (float): Initial interest rate
    kappa (float): Rate of mean reversion
    theta (float): Long-term mean rate
    sigma (float): Volatility of interest rates
    T (float): Time to maturity (in years)
    num_paths (int): Number of paths to simulate
    """
    plt.figure(figsize=(10, 6))
    
    for _ in range(num_paths):
        rates = cir_model(r0, kappa, theta, sigma, T)
        plt.plot(np.linspace(0, T, len(rates)), rates, label="Simulated Path")
    
    plt.title("Simulated Interest Rate Paths (Cox-Ingersoll-Ross Model)")
    plt.xlabel("Time (Years)")
    plt.ylabel("Interest Rate (%)")
    plt.legend()
    plt.show()

# Example usage:
# r0 = 0.03  # Initial interest rate
# kappa = 0.1  # Mean reversion speed
# theta = 0.05  # Long-term mean rate
# sigma = 0.02  # Volatility of interest rates
# T = 1  # Time to maturity (1 year)
# plot_interest_rate_paths(r0, kappa, theta, sigma, T)
