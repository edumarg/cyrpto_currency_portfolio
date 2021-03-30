from requests import Request, Session
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
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '50',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        pprint(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        pprint(e)
