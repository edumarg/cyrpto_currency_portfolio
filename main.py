import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

from decouple import config
from prettyprinter import pprint

import GUI

# For the API documentation go to
# https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide

API_KEY = config("API_KEY")
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '50',
    'convert': 'USD',
    "CMC_PRO_API_KEY": API_KEY,
}

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


def get_api_info():
    api_request = requests.get(url=url, params=parameters)
    data = json.loads(api_request.content)
    return data["data"]


def add_coin_msg_to_gui(coin_msg):
    coin_frame = GUI.Frame(GUI.second_frame,
                           relief='ridge',
                           borderwidth=2,
                           bg='#F2F2F2')
    coin_frame.pack(pady=(10, 0),
                    padx=(5, 5),
                    fill='x',
                    anchor='center')
    display_coin_msg = GUI.Label(coin_frame,
                                 text=coin_msg,
                                 anchor='w',
                                 font=('Time New Roman', '13', 'bold underline'),
                                 bg='#F2F2F2')
    display_coin_msg.pack(fill='x')


def show_portfolio_profit_loss_on_gui(profit_loos):
    # view client version on bottom left corner
    portfolio_profit_loos_label = GUI.Label(GUI.root,
                                            text="Portfolio Total Profit/Loos: ${0:.2f}".format(profit_loos),
                                            font=('Time New Roman', '9', 'bold'),
                                            bg="white")
    portfolio_profit_loos_label.pack(pady=(5, 0),
                                     anchor='e')


def format_data():
    try:
        coins = get_api_info()
        portfolio_profit_loos = 0
        for coin in coins:
            for sym in my_portfolio:
                if sym["symbol"] == coin["symbol"]:
                    total_paid = sym["price_payed_per_unit"] * sym["amount_owned"]
                    total_current_value = sym["amount_owned"] * float(coin["quote"]["USD"]["price"])
                    profit = total_current_value - total_paid
                    profit_percentage = profit / total_paid * 100
                    profit_per_coin = float(coin["quote"]["USD"]["price"]) - sym["price_payed_per_unit"]
                    # my_coin = {"Name": coin["name"],
                    #            "Symbol": coin["symbol"],
                    #            "Rank": coin["cmc_rank"],
                    #            "Current Price": "${0:.2f}".format(float(coin["quote"]["USD"]["price"])),
                    #            "24 Hour Change:": "{0:.2f}%".format(float(coin["quote"]["USD"]["percent_change_24h"])),
                    #            "Paid per coin": "${0:.2f}".format(float(sym["price_payed_per_unit"])),
                    #            "Amount Owned": f'{sym["amount_owned"]} units',
                    #            "Total current value": "${0:.2f}".format(total_current_value),
                    #            "Total Paid": "${0:.2f}".format(total_paid),
                    #            "Profit/Loss per coin:": "${0:.2f}".format(profit_per_coin),
                    #            "Profit/Loss:": "${0:.2f}".format(profit),
                    #            "Profit/Loss percentage": "{0:.2f}%".format(profit_percentage),
                    #            }
                    my_coin_msg = f'Name: {coin["name"]} \n' \
                                  f'Symbol: {coin["symbol"]} \n' \
                                  f'Rank: {coin["cmc_rank"]} \n' \
                                  f'Current Price: ${float(coin["quote"]["USD"]["price"]):.2f} \n' \
                                  f'24 Hour Change: {float(coin["quote"]["USD"]["percent_change_24h"]):.2f}% \n' \
                                  f'Paid per coin: ${sym["price_payed_per_unit"]:.2f} \n' \
                                  f'Amount Owned: {sym["amount_owned"]} units \n' \
                                  f'Total current value: ${total_current_value:.2f} \n' \
                                  f'Total Paid: ${total_paid:.2f} \n' \
                                  f'Profit/Loss per coin:${profit_per_coin:.2f} \n' \
                                  f'Profit/Loss: ${profit:.2f} \n' \
                                  f'Profit/Loss percentage: {profit_percentage:.2f}%'
                    portfolio_profit_loos += profit
                    # display_coin_msg = Label(root, text=my_coin_msg)
                    # display_coin_msg.pack()
                    add_coin_msg_to_gui(my_coin_msg)
        # print("Portfolio Total Profit/Loos: ", "${0:.2f}".format(portfolio_profit_loos))
        show_portfolio_profit_loss_on_gui(portfolio_profit_loos)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        pprint(e)


if __name__ == "__main__":
    # Clear command line window
    os.system('cls')
    format_data()
    print("start")
    GUI.root.mainloop()
    print("GUI")
