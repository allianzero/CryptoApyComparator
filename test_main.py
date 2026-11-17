"""Tests for CryptoApyComparator."""
import unittest
from main import summarize


class TestTool(unittest.TestCase):
    def test_main_function(self):
        r = summarize([8.5, 12.0, 9.25])
        self.assertEqual(r['count'], 3)
        self.assertAlmostEqual(r['mean'], 9.9166666667, places=6)
        self.assertEqual(r['min'], 8.5)
        self.assertEqual(r['max'], 12.0)


if __name__ == "__main__":
    unittest.main()
