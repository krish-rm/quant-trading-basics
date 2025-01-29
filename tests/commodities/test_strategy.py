# test_strategy.py
# This test ensures that commodity trading strategies (e.g., mean reversion, momentum) work as expected.

import unittest
from src.commodities import strategy

class TestCommodityTradingStrategy(unittest.TestCase):
    def test_mean_reversion(self):
        prices = [100, 102, 101, 98, 95, 96, 97]
        signal = strategy.mean_reversion_strategy(prices, threshold=2)

        expected_signal = ['Hold', 'Hold', 'Sell', 'Buy', 'Buy', 'Hold', 'Hold']
        self.assertEqual(signal, expected_signal)

    def test_momentum_strategy(self):
        prices = [100, 102, 105, 110, 115, 120]
        signal = strategy.momentum_strategy(prices, lookback=3)

        expected_signal = ['Hold', 'Hold', 'Buy', 'Buy', 'Buy', 'Buy']
        self.assertEqual(signal, expected_signal)

if __name__ == "__main__":
    unittest.main()
