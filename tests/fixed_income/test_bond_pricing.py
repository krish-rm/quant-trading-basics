# test_bond_pricing.py
# This test ensures that the bond pricing model correctly calculates present values and yield-to-maturity (YTM).

import unittest
from src.fixed_income import bond_pricing

class TestBondPricing(unittest.TestCase):
    def test_present_value(self):
        face_value = 1000
        coupon_rate = 0.05
        market_rate = 0.04
        years = 5
        
        price = bond_pricing.present_value(face_value, coupon_rate, market_rate, years)
        expected_price = 1045.22  # Approximate theoretical price
        self.assertAlmostEqual(price, expected_price, places=2)

    def test_ytm(self):
        bond_price = 950
        face_value = 1000
        coupon_rate = 0.05
        years = 5

        ytm = bond_pricing.calculate_ytm(bond_price, face_value, coupon_rate, years)
        expected_ytm = 0.06  # Approximate expected YTM (6%)
        self.assertAlmostEqual(ytm, expected_ytm, places=2)

if __name__ == "__main__":
    unittest.main()
