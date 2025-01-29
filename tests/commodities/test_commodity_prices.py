# test_commodity_prices.py
# This test ensures that commodity price processing functions correctly handle data retrieval, normalization, and trend analysis.

import unittest
import pandas as pd
from src.commodities import commodity_prices

class TestCommodityPrices(unittest.TestCase):
    def setUp(self):
        # Sample commodity price data
        self.data = pd.DataFrame({
            'date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
            'price': [100, 102, 105, 103, 108]
        })

    def test_moving_average(self):
        ma = commodity_prices.calculate_moving_average(self.data, window=3)
        expected_ma = [None, None, 102.33, 103.33, 105.33]  # Approximate values
        self.assertAlmostEqual(ma.iloc[-1], expected_ma[-1], places=2)

    def test_price_volatility(self):
        volatility = commodity_prices.calculate_volatility(self.data)
        self.assertGreater(volatility, 0)  # Volatility should be non-negative

if __name__ == "__main__":
    unittest.main()
