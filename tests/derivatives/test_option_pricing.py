# test_option_pricing.py
# This test ensures that the Black-Scholes model computes the correct option prices.

import unittest
import numpy as np
from src.derivatives import option_pricing

class TestOptionPricing(unittest.TestCase):
    def test_black_scholes_call(self):
        S = 100  # Stock price
        K = 100  # Strike price
        T = 1    # Time to expiration (1 year)
        r = 0.05 # Risk-free rate
        sigma = 0.2  # Volatility

        call_price = option_pricing.black_scholes(S, K, T, r, sigma, option_type="call")
        expected_price = 10.45  # Approximate theoretical price
        self.assertAlmostEqual(call_price, expected_price, places=2)

    def test_black_scholes_put(self):
        S = 100
        K = 100
        T = 1
        r = 0.05
        sigma = 0.2

        put_price = option_pricing.black_scholes(S, K, T, r, sigma, option_type="put")
        expected_price = 5.57  # Approximate theoretical price
        self.assertAlmostEqual(put_price, expected_price, places=2)

if __name__ == "__main__":
    unittest.main()
