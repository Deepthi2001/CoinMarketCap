import requests # helps us to get the data
import json # helps us to pass the data

api_requests = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=e428c45e-383e-4db2-a75a-2c6edd7a97b4")
api = json.loads(api_requests.content)
coins = [
        {
            "symbol": "BTC",
            "no_of_coins": 2,
            "price_per_coin": 3200
        },
        {
            "symbol": "EOS",
            "no_of_coins": 100,
            "price_per_coin": 2.05

        },
        {
            "symbol": "XRP",
            "no_of_coins": 20,
            "price_per_coin": 100
        }
    ]
'''for i in range(5):
    print(api['data'][i]['symbol'])
    print("{0:.2f}".format(api['data'][i]['quote']['USD']['price']))
    print("--------------------")'''

net_pl_amount = 0
for i in range(5):
    for coin in coins:
        if api['data'][i]['symbol'] == coin['symbol']:
            total_paid = coin['no_of_coins'] * coin['price_per_coin']
            current_price = coin['no_of_coins'] * api['data'][i]['quote']['USD']['price']
            pl_per_coin = api['data'][i]['quote']['USD']['price'] - coin['price_per_coin']
            pl_amount = pl_per_coin * coin['no_of_coins']
            net_pl_amount += pl_amount

            print(api['data'][i]['name'] + "-" + api['data'][i]['symbol'])
            print("Price - {0:.2f}".format(api['data'][i]['quote']['USD']['price']))
            print("Total number of coins: ", coin["no_of_coins"])
            print("Total amount invested: ", "{0:0.2f}".format(total_paid))
            print("Current value: ", "{0:0.2f}".format(current_price))

            if current_price > total_paid:
                print("You have profit of {0:0.2f} per coin and total of {1:0.2f}".format(pl_per_coin, pl_amount))
            else:
                print("You have have {0:0.2f} per coin and total of {1:0.2f}".format(pl_per_coin, pl_amount))
            print("--------------------")
print("And hence the net amount for portfolio is {0:0.2f}".format(net_pl_amount))
