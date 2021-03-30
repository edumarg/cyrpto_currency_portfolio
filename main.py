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
        "CMC_PRO_API_KEY": API_KEY,
    }
    try:
        api_request = requests.get(url=url, params=parameters)
        data = json.loads(api_request.content)
        coins = data["data"]
        my_portfolio = [
            {
                "symbol": "BTC",
                "amount_owned": 2000,
                "price_payed_per_unit": 20.0
            },
            {
                "symbol": "ETH",
                "amount_owned": 500,
                "price_payed_per_unit": 2.0
            },
            {
                "symbol": "XPR",
                "amount_owned": 1500,
                "price_payed_per_unit": 0.1
            },
            {
                "symbol": "XLM",
                "amount_owned": 2000,
                "price_payed_per_unit": 0.2
            },
            {
                "symbol": "EOS",
                "amount_owned": 1000,
                "price_payed_per_unit": 2.0
            },
        ]
        portfolio_profit_loos = 0

        for coin in coins:
            for sym in my_portfolio:
                if sym["symbol"] == coin["symbol"]:
                    total_paid = sym["price_payed_per_unit"] * sym["amount_owned"]
                    total_current_value = sym["amount_owned"] * float(coin["quote"]["USD"]["price"])
                    profit = total_current_value - total_paid
                    profit_percentage = profit / total_paid * 100
                    profit_per_coin = float(coin["quote"]["USD"]["price"]) - sym["price_payed_per_unit"]
                    print("---------------------------------------------")
                    my_coin = {"Name": coin["name"],
                               "Symbol": coin["symbol"],
                               "Rank": coin["cmc_rank"],
                               "Current Price": "${0:.2f}".format(float(coin["quote"]["USD"]["price"])),
                               "24 Hour Change:": "{0:.2f}%".format(float(coin["quote"]["USD"]["percent_change_24h"])),
                               "Paid per coin": "${0:.2f}".format(float(sym["price_payed_per_unit"])),
                               "Amount Owned": f'{sym["amount_owned"]} units',
                               "Total current value": "${0:.2f}".format(total_current_value),
                               "Total Paid": "${0:.2f}".format(total_paid),
                               "Profit/Loss per coin:": "${0:.2f}".format(profit_per_coin),
                               "Profit/Loss:": "${0:.2f}".format(profit),
                               "Profit/Loss percentage": "{0:.2f}%".format(profit_percentage),
                               }
                    portfolio_profit_loos += profit
                    pprint(my_coin)
        print("---------------------------------------------")
        print("Portfolio Total Profit/Loos: ", "${0:.2f}".format(portfolio_profit_loos))

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        pprint(e)
