# test_yield_curve.py
# This test ensures that the yield curve construction model correctly interpolates and estimates yields.

import unittest
from src.fixed_income import yield_curve

class TestYieldCurve(unittest.TestCase):
    def test_linear_interpolation(self):
        terms = [1, 3, 5, 10]
        yields = [0.02, 0.025, 0.03, 0.035]  # Yield for given maturities

        interpolated_yield = yield_curve.linear_interpolate(4, terms, yields)
        expected_yield = 0.0275  # Expected interpolated yield at 4 years
        self.assertAlmostEqual(interpolated_yield, expected_yield, places=4)

    def test_bootstrap_yield_curve(self):
        bond_prices = [980, 950, 920]  # Simulated bond market prices
        face_values = [1000, 1000, 1000]
        coupon_rates = [0.02, 0.025, 0.03]
        years = [1, 3, 5]

        yield_curve_data = yield_curve.bootstrap_yield_curve(bond_prices, face_values, coupon_rates, years)
        expected_curve = {1: 0.0204, 3: 0.0273, 5: 0.0312}  # Expected interpolated rates
        for key in expected_curve:
            self.assertAlmostEqual(yield_curve_data[key], expected_curve[key], places=4)

if __name__ == "__main__":
    unittest.main()
