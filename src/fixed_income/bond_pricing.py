# bond_pricing.py
# Bond pricing models: Yield to Maturity. This script implements a basic bond pricing model, calculating the price of a bond based on its Yield to Maturity (YTM).

import numpy as np

def bond_price(face_value, coupon_rate, periods, ytm):
    """
    Calculate the price of a bond based on Yield to Maturity (YTM).

    Args:
    face_value (float): The face value or par value of the bond
    coupon_rate (float): The annual coupon rate (as a decimal, e.g., 0.05 for 5%)
    periods (int): The number of periods (years) to maturity
    ytm (float): The Yield to Maturity (as a decimal, e.g., 0.03 for 3%)

    Returns:
    float: The price of the bond
    """
    # Calculate the coupon payment
    coupon_payment = face_value * coupon_rate
    
    # Calculate the present value of the coupon payments
    coupon_pv = sum([coupon_payment / (1 + ytm)**t for t in range(1, periods + 1)])
    
    # Calculate the present value of the face value (principal)
    face_value_pv = face_value / (1 + ytm)**periods
    
    # Bond price is the sum of the present values
    price = coupon_pv + face_value_pv
    
    return price

# Example usage:
# bond_price_value = bond_price(1000, 0.05, 10, 0.03)
