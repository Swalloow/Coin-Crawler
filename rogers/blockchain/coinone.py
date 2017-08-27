from datetime import datetime

from config import Source
from rogers.model.models import Coinone
import requests

from utils.slack import send_message


class ParserCoinone:
    def __init__(self):
        self.model = Coinone
        self.url = Source.COINONE_URI
        self.currency = ["btc", "eth"]

    def get_response(self, params):
        try:
            response = requests.get(self.url, params)
            return response

        except requests.exceptions.ConnectionError:
            send_message("#data-monitoring", "Connection Failed!")
            return "Connection Failed!"

    def parse(self, response, currency):
        result = response.json()
        price = result["last"]
        volume = result["volume"]
        self.model = Coinone(datetime.utcnow(), price, volume, currency)
        return self.model
