# test_data_processing.py
# This test validates the data processing module to ensure that data is loaded correctly and daily returns are calculated as expected.

import unittest
import pandas as pd
import numpy as np
from src.equities import data_processing

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        # Create a sample dataset
        data = {
            "Date": pd.date_range(start="2023-01-01", periods=5, freq="D"),
            "Price": [100, 102, 101, 105, 107]
        }
        self.df = pd.DataFrame(data)
        self.df.set_index("Date", inplace=True)

    def test_calculate_daily_returns(self):
        processed_data = data_processing.calculate_daily_returns(self.df.copy())
        expected_returns = [np.nan, 0.02, -0.0098, 0.0396, 0.0190]
        
        # Check if NaN value is in first row and rest are approximately correct
        self.assertTrue(np.isnan(processed_data.iloc[0]["Daily Return"]))
        for i in range(1, len(expected_returns)):
            self.assertAlmostEqual(processed_data.iloc[i]["Daily Return"], expected_returns[i], places=4)

if __name__ == "__main__":
    unittest.main()
