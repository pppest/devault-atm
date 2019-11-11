import requests
import json
import sys
import time


def get_coingecko_price(coin, pair):
    api = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={pair}"
    request = requests.get(api)
    json_data = json.loads(request.text)
    coin_price = json_data[f'{coin}'][f'{pair}']
    return coin_price


# fee in percentage
def price_with_fee(coin, pair, fee, decimals):
    price_with_fee = round(get_coingecko_price(coin, pair) * (1 + fee / 100),
                           decimals)
    return price_with_fee
