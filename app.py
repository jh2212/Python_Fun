from flask import Flask, render_template
import requests
import pandas as pd

from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)

API_KEY = 'X3LLF32S7AE1KI1L'
BASE_URL = 'https://www.alphavantage.co/query'

def get_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    time_series = data.get('Time Series (5min)', {})

    df = pd.DataFrame(time_series).T
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df = df.astype(float)
    
    return df

@app.route('/')
def index():
    symbol = 'AAPL'
    df = get_stock_data(symbol)
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
