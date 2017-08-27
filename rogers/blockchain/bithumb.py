from datetime import datetime

from config import Source
from utils.slack import send_message
from rogers.model.models import Bithumb
import requests


class ParserBithumb:
    def __init__(self):
        self.model = Bithumb
        self.url = Source.BITHUMB_URI
        self.currency = ["BTC", "ETH"]

    def get_response(self, params):
        try:
            response = requests.get(self.url, params)
            return response

        except requests.exceptions.ConnectionError:
            send_message("#data-monitoring", "Connection Failed!")
            return "Connection Failed!"

    def parse(self, response, currency):
        result = response.json()["data"]
        price = result["closing_price"]
        volume = result["units_traded"]
        self.model = Bithumb(datetime.utcnow(), price, volume, currency)
        return self.model
