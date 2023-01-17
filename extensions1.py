import requests
import json
from config import coin

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            base_tiker = coin[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            quote_tiker = coin[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        url = f"https://api.apilayer.com/fixer/convert?to={quote_tiker}&from={base_tiker}&amount={amount}"
        payload = {}
        headers = {
            "apikey": "usWhbdEJkOmj204GTPoUOm35SyM8Xw6Q"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        result = json.loads(response.content)
        return result
