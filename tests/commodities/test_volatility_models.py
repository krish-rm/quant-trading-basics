# test_volatility_models.py
# This test ensures that commodity volatility models (e.g., GARCH, historical volatility) work correctly.

import unittest
import numpy as np
from src.commodities import volatility_models

class TestCommodityVolatility(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.price_changes = np.random.normal(0, 1, 100)  # Simulated daily returns

    def test_historical_volatility(self):
        vol = volatility_models.historical_volatility(self.price_changes, window=10)
        self.assertGreater(vol, 0)  # Volatility should always be positive

    def test_garch_model(self):
        simulated_vol = volatility_models.garch_model(self.price_changes)
        self.assertGreater(simulated_vol, 0)  # Volatility from GARCH should be positive

if __name__ == "__main__":
    unittest.main()
