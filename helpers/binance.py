import requests

# Function to fetch historical data
def fetch_historical_data(symbol, interval, limit=100):
    url = f'https://fapi.binance.com/fapi/v1/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Function to calculate Fibonacci levels
def calculate_fibonacci_levels(symbol, interval):
    data = fetch_historical_data(symbol, interval, limit=100)
    previous_candle = data[-2]
    high = float(previous_candle[2])
    low = float(previous_candle[3])
    close = float(previous_candle[4])
    diff = high - low
    levels = {
        '300%': close + diff * 3.0,
        '261.8%': close + diff * 2.618,
        '238.2%': close + diff * 2.382,
        '200%': close + diff * 2.0,
        '178.6%': close + diff * 1.786,
        '161.8%': close + diff * 1.618,
        '150%': close + diff * 1.5,
        '138.2%': close + diff * 1.382,
        '123.6%': close + diff * 1.236,
        '100%': close + diff * 1.0,
        '78.6%': close + diff * 0.786,
        '61.8%': close + diff * 0.618,
        '50%': close + diff * 0.5,
        '38.2%': close + diff * 0.382,
        '23.6%': close + diff * 0.236,
        '0%': close,
        '-23.6%': close - diff * 0.236,
        '-38.2%': close - diff * 0.382,
        '-50%': close - diff * 0.5,
        '-61.8%': close - diff * 0.618,
        '-78.6%': close - diff * 0.786,
        '-100%': close - diff,
        '-123.6%': close - diff * 1.236,
        '-138.2%': close - diff * 1.382,
        '-150%': close - diff * 1.5,
        '-161.8%': close - diff * 1.618,
        '-178.6%': close - diff * 1.786,
        '-200%': close - diff * 2.0,
        '-238.2%': close - diff * 2.382,
        '-261.8%': close - diff * 2.618,
        '-300%': close - diff * 3.0
    }
    return {
        "levels": levels,
        "currentPrice": close
    }