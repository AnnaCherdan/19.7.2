import requests
# import json


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

    def get_multiple_symbols_full_data(self, fsym: str, tsym: str):
        """Полные данные по нескольким валютным наименованиям."""
        res = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={fsym}&tsyms={tsym}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_generate_custom_average(self, fsym: str, tsym: str, e: str):
        """Генерация средних данных по конвертируемой валютной паре."""
        res = requests.get(f'https://min-api.cryptocompare.com/data/generateAvg?fsym={fsym}&tsym={tsym}&e={e}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_mapping_from_symbol(self, fsym: str):
        """Сопоставление криптовалют по символьному наименованию."""
        res = requests.get(f'https://min-api.cryptocompare.com/data/v2/pair/mapping/fsym?fsym={fsym}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
