# test_backtesting.py
# This test ensures that backtesting logic computes portfolio returns properly.

import unittest
import pandas as pd
from src.equities import backtesting

class TestBacktesting(unittest.TestCase):
    def setUp(self):
        # Sample trading data
        data = {
            "Date": pd.date_range(start="2023-01-01", periods=5, freq="D"),
            "Price": [100, 105, 110, 108, 112],
            "Position": [0, 1, 1, 0, 1]  # Buy on second day, sell on fourth, buy on fifth
        }
        self.df = pd.DataFrame(data)
        self.df.set_index("Date", inplace=True)

    def test_backtest_strategy(self):
        initial_capital = 10000
        backtested_data = backtesting.backtest_strategy(self.df.copy(), initial_capital)

        # Check if portfolio value is calculated
        self.assertIn("Portfolio Value", backtested_data.columns)
        self.assertGreater(backtested_data["Portfolio Value"].iloc[-1], initial_capital)

if __name__ == "__main__":
    unittest.main()
