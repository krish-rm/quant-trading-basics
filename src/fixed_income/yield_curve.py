# yield_curve.py
# Yield curve construction models. This script demonstrates how to construct a yield curve using a simple method, such as bootstrapping, from a set of market bond prices and corresponding yields.

import numpy as np
import pandas as pd

def bootstrap_yield_curve(bond_prices, maturities, face_value=1000, coupon_rate=0.05):
    """
    Construct a yield curve using bootstrapping from bond prices and maturities.

    Args:
    bond_prices (list): List of bond prices
    maturities (list): List of maturities (in years)
    face_value (float): The face value or par value of the bond (default is 1000)
    coupon_rate (float): The annual coupon rate (as a decimal, e.g., 0.05 for 5%)

    Returns:
    pd.DataFrame: A DataFrame with maturities and corresponding spot rates (yields)
    """
    spot_rates = []
    
    for i in range(len(bond_prices)):
        price = bond_prices[i]
        maturity = maturities[i]
        
        if i == 0:
            # First bond: Use simple formula for the first spot rate (for a zero-coupon bond)
            spot_rate = (face_value / price) ** (1 / maturity) - 1
        else:
            # Subsequent bonds: Use the bootstrapping technique
            discounted_cash_flows = sum([(face_value * coupon_rate) / (1 + r) ** t for t, r in enumerate(spot_rates, 1)])
            spot_rate = (face_value + discounted_cash_flows) / price - 1
        
        spot_rates.append(spot_rate)
    
    # Create a DataFrame with the results
    yield_curve = pd.DataFrame({
        'Maturity (Years)': maturities,
        'Spot Rate (%)': np.array(spot_rates) * 100
    })
    
    return yield_curve

# Example usage:
# bond_prices = [950, 980, 1000]
# maturities = [1, 2, 3]
# yield_curve_df = bootstrap_yield_curve(bond_prices, maturities)
