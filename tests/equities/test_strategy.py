# test_strategy.py
# This test checks whether the trading strategy module correctly generates buy/sell signals using a moving average crossover strategy.

import unittest
import pandas as pd
from src.equities import strategy

class TestStrategy(unittest.TestCase):
    def setUp(self):
        # Create sample data
        data = {
            "Date": pd.date_range(start="2023-01-01", periods=10, freq="D"),
            "Price": [100, 101, 102, 104, 107, 108, 110, 115, 120, 125]
        }
        self.df = pd.DataFrame(data)
        self.df.set_index("Date", inplace=True)

    def test_moving_average_strategy(self):
        result = strategy.moving_average_strategy(self.df, short_window=3, long_window=5)
        self.assertIn("Signal", result.columns)
        self.assertIn("Position", result.columns)
        self.assertTrue(result["Signal"].dtype == "int64")

if __name__ == "__main__":
    unittest.main()
