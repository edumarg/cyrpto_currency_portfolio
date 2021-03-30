# from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from decouple import config
from prettyprinter import pprint

# Clear command line window
os.system('clear')

if __name__ == "__main__":
    os.system('cls')
    API_KEY = config("API_KEY")
    # For the API documentation go to
    # https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '50',
        'convert': 'USD',
    }
    try:
        api_request = requests.get(
            f'{url}?start={parameters["start"]}&limit={parameters["limit"]}&convert={parameters["convert"]}&CMC_PRO_API_KEY={API_KEY}')
        data = json.loads(api_request.content)
        coins = data["data"]
        for coin in coins:
            pprint({'Name': coin["name"],
                    'Symbol': coin["symbol"],
                    "price (USD)": coin["quote"]["USD"]["price"]})

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        pprint(e)
