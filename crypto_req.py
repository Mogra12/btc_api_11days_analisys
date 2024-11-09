from requests import get
import plotly.graph_objects as go
from datetime import datetime

class BTC:
    url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=10'
    response = get(url)
    data = response.json()

    def __init__(self):
        if 'Data' in self.data and 'Data' in self.data['Data']:

            self.high = [item['high'] for item in self.data['Data']['Data']]
            self.low = [item['low'] for item in self.data['Data']['Data']]
            self.open = [item['open'] for item in self.data['Data']['Data']]
            self.close = [item['close'] for item in self.data['Data']['Data']]
            self.date = [item['time'] for item in self.data['Data']['Data']]
        else:
            print("Data not found")
            self.high = []
            self.low = []
            self.open = []
            self.close = []
            self.date = []

    def get_high(self):
        return self.high
    
    def get_low(self):
        return self.low
    
    def get_open(self):
        return self.open
    
    def get_close(self):
        return self.close
    
    def get_date(self):
        return self.date

btc = BTC()

dates = [datetime.utcfromtimestamp(timestamp) for timestamp in btc.get_date()]

def fig_show(dates):
    fig = go.Figure(data=[go.Candlestick(x=dates,
                                        open=btc.open, high=btc.high,
                                        low=btc.low,close=btc.close)])
    fig.update_layout(title="BTC 11 days",
                        xaxis_title="Days",
                        yaxis_title="Price (USD)",
                        shapes=[dict(
                            x0='2024-11-05', x1='2024-11-05',
                            y0=0, y1=1,
                            xref='x', yref='paper',
                            line_width=2, line_color='black'
                        )],
                        annotations=[dict(
                            x='2024-11-05', y=0.05, yref='paper',
                            showarrow=False,
                            xanchor='left',
                            text="Increase Period Begins"
                        )]
                    )
    fig.show()

fig_show(dates)
