import requests
from odoo import http
from datetime import datetime

def get_bitcoin_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "30",
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['prices']

def epoch_to_date(epoch):
    return datetime.fromtimestamp(epoch / 1000).strftime('%Y-%m-%d')

class BtcPriceController(http.Controller):
    @http.route('/btc_price', type='json', auth='public', website=True)
    def get_btc_price(self):
        res = {}
        data = get_bitcoin_data()
        res['date'] = [epoch_to_date(d[0]) for d in data]
        res['price'] = [d[1] for d in data]
        return res