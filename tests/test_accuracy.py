import os
from unittest import TestCase

import pandas as pd

from Matcha import calculate_accuracy


class TestMetrics(TestCase):

    def test_accuracy(self):
        path = "datasets/ps4-madden21.csv"
        outcomes = pd.read_csv(path)  
        res = calculate_accuracy(outcomes)
        self.assertEqual(round(res, 2), 0.62)
        