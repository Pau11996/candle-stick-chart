import logging
from datetime import datetime, date
import matplotlib.pyplot as plt

import mplfinance as mpf

from consts import CANDLES_PERIOD
from services import build_dataframe_for_candlesticks, calculate_ema, convert_date


def candlestick_chart(
        csv_path: str,
        time_period: str = '5MIN',
        start_date_period: datetime = None,
        end_date_period: datetime = None
):
    dataframe = build_dataframe_for_candlesticks(csv_path, time_period, start_date_period, end_date_period)

    dataframe['EMA'] = calculate_ema(dataframe, window=20)

    mpf.plot(dataframe, type='candle', style='charles', title="Candlestick Chart with EMA", ylabel='Price', mav=5)
    plt.show()


if __name__ == "__main__":
    try:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        candle_time = input("Enter candlestick time (e.g., '1H' for 1 hour, '5T' for 5 minutes): ")

        if candle_time not in CANDLES_PERIOD:
            raise ValueError('Candles period must  be 1H or 5T')

        date: dict[str, date] = convert_date(start_date, end_date)

        candlestick_chart(
            'prices.csv',
            time_period=candle_time,
            start_date_period=date.get('start_date'),
            end_date_period=date.get('end_date')
        )
    except ValueError as e:
        logging.error(f"You specified wrong date period or candlestick time: {e}")

