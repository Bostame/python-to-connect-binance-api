# importing required library
import threading
from operator import itemgetter
import requests

# Getting response from market
response = requests.get(' https://api.binance.com/api/v3/ticker/price')

# Setting Up interval
update_timer = 10

# Defining function for log price
def my_binance():
    data = response.json()
    data = [dict([a, float(x)] if a == "price" else [a, x] for a, x in b.items()) for b in data]
    data = sorted(data, key=itemgetter('price'), reverse=True)
    for d in data:
        symbol = d["symbol"]
        price = d["price"]
        print("{} : {}".format(symbol, price))

    print("\n========New Price is loading==========\n")
    threading.Timer(update_timer, my_binance).start()


my_binance()
