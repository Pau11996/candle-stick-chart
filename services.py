from datetime import datetime
import pandas as pd
from pandas import DataFrame


def convert_date(start_date_str: str, end_date_str: str) -> dict[str, datetime]:
    date_format = '%Y-%m-%d'
    start_date_converted = datetime.strptime(start_date_str, date_format)
    end_date_converted = datetime.strptime(end_date_str, date_format)
    return {'start_date': start_date_converted, 'end_date': end_date_converted}


def calculate_ema(data, window=20, column='Close'):
    # but will be simpler: data[column].ewm(span=window, adjust=False).mean()
    ema_values = []
    multiplier = 2 / (window + 1)

    initial_sma = data[column].iloc[:window].mean()
    ema_values.extend([initial_sma] * window)

    for i in range(window, len(data)):
        ema = (data[column].iloc[i] - ema_values[-1]) * multiplier + ema_values[-1]
        ema_values.append(ema)

    return pd.Series(ema_values, index=data.index)


def build_dataframe_for_candlesticks(
        csv_path: str,
        candles_time: str,
        start_datetime: datetime,
        end_datetime: datetime
) -> DataFrame:
    df = pd.read_csv(csv_path)
    df['datetime'] = pd.to_datetime(df['TS'])

    if start_datetime and end_datetime:
        df = df[(df['datetime'] >= start_datetime) & (df['datetime'] <= end_datetime)]

    if df.empty:
        raise ValueError('Empty dataframe. Specify correct date period')

    resampled_df = df.resample(candles_time, on='datetime').agg({
        'PRICE': ['first', 'max', 'min', 'last']
    })

    resampled_df.columns = ['Open', 'High', 'Low', 'Close']
    resampled_df.dropna(inplace=True)

    return resampled_df
