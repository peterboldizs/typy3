__author__ = 'fnxuser'

import unittest


class TestingFunctions(unittest.TestCase):
    def avg(values):
        """
        >>> print(avg([20,30,70]))
        40.0
    """
        return sum(values) / len(values)

    def test_avg(self):
        self.assertEqual(self.avg([20, 30, 70]), 40.0)


unittest.main()
