import requests
import json


class CryptocompareAn:

    def get_price(self, fsym: str, tsym: str):
        """Конвертация валюты fsym в валюту tsym"""
        res = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={fsym}&tsyms={tsym}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_invalid_currency(self, fsym: str, tsym: str):
        """Ошибка конвертации валюты fsym в отстутствующую валюту tsym"""
        res = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={fsym}&tsyms={tsym}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_multiple_symbols_price(self, fsym: str, tsym: str):
        """Конвертации нескольких валют fsym в несколько валют tsym"""
        res = requests.get(f'https://min-api.cryptocompare.com/data/pricemulti?fsyms={fsym}&tsyms={tsym}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
