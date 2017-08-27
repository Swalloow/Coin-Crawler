from datetime import datetime

from config import Source
from rogers.model.models import Korbit
import requests

from utils.slack import send_message


class ParserKorbit:
    def __init__(self):
        self.model = Korbit
        self.url = Source.KORBIT_URI
        self.currency = ["btc_krw", "eth_krw"]

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
        self.model = Korbit(datetime.utcnow(), price, volume, currency)
        return self.model
