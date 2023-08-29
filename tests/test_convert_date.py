import unittest
from datetime import datetime

from services import convert_date


class TestConvertDate(unittest.TestCase):

    def test_convert_date_valid(self):
        start_date_str = '2023-08-01'
        end_date_str = '2023-08-15'
        expected_result = {
            'start_date': datetime(2023, 8, 1),
            'end_date': datetime(2023, 8, 15)
        }
        result = convert_date(start_date_str, end_date_str)
        self.assertEqual(result, expected_result)

    def test_convert_date_invalid_format(self):
        start_date_str = '2023/08/01'
        end_date_str = '2023-08-15'
        with self.assertRaises(ValueError):
            convert_date(start_date_str, end_date_str)
