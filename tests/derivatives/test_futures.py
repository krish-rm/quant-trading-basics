# test_futures.py
# This test checks whether the futures pricing model correctly calculates the fair value of futures contracts.

import unittest
from src.derivatives import futures

class TestFuturesPricing(unittest.TestCase):
    def test_futures_price(self):
        S = 100  # Spot price of the underlying asset
        r = 0.05 # Risk-free interest rate
        T = 1    # Time to maturity (1 year)
        storage_cost = 2  # Cost of carrying the asset

        calculated_price = futures.futures_price(S, r, T, storage_cost)
        expected_price = 105.13  # Approximate expected fair value
        self.assertAlmostEqual(calculated_price, expected_price, places=2)

if __name__ == "__main__":
    unittest.main()
