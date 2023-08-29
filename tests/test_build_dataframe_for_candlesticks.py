import unittest
import pandas as pd
from datetime import datetime

from services import build_dataframe_for_candlesticks


class TestBuildDataFrameForCandlesticks(unittest.TestCase):

    def setUp(self):
        self.csv_path = '../prices.csv'
        self.candles_time = '1H'
        self.start_datetime = datetime(2023, 4, 10)
        self.end_datetime = datetime(2023, 4, 15)

    def test_build_dataframe_empty(self):
        data = {'TS': [], 'PRICE': []}
        empty_df = pd.DataFrame(data)

        with self.assertRaises(ValueError):
            build_dataframe_for_candlesticks(
                self.csv_path, self.candles_time, self.start_datetime, self.end_datetime
            )
