from tkinter import *
import requests # helps us to get the data
import json # helps us to pass the data

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap('favicon.ico')

def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"

def my_portfolio():
    api_requests = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=e428c45e-383e-4db2-a75a-2c6edd7a97b4")
    api = json.loads(api_requests.content)

    coins = [
        {
            "symbol": "BTC",
            "no_of_coins": 2,
            "price_per_coin": 3200
        },
        {
            "symbol": "ETH",
            "no_of_coins": 10,
            "price_per_coin": 5600
        },
        {
            "symbol": "USDT",
            "no_of_coins": 125,
            "price_per_coin": 1550
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
    c = 1
    net_pl_amount = 0
    total_curr = 0
    total_amount_paid = 0

    for i in range(300):
        for coin in coins:
            if api['data'][i]['symbol'] == coin['symbol']:
                total_paid = coin['no_of_coins'] * coin['price_per_coin']
                current_price = coin['no_of_coins'] * api['data'][i]['quote']['USD']['price']
                pl_per_coin = api['data'][i]['quote']['USD']['price'] - coin['price_per_coin']
                pl_amount = pl_per_coin * coin['no_of_coins']

                net_pl_amount += pl_amount
                total_curr += current_price
                total_amount_paid += total_paid

                '''print(api['data'][i]['name'] + "-" + api['data'][i]['symbol'])
                print("Price - {0:.2f}".format(api['data'][i]['quote']['USD']['price']))
                print("Total number of coins: ", coin["no_of_coins"])
                print("Total amount invested: ", "{0:0.2f}".format(total_paid))
                print("Current value: ", "{0:0.2f}".format(current_price))'''

                name = Label(pycrypto, text=api['data'][i]['name'], bg="light grey", fg="black", font=("Arial Bold", 10), padx="5", pady="5", borderwidth=2, relief="groove")
                name.grid(row=c, column=0, sticky=N+S+E+W)

                price = Label(pycrypto, text="{0:.2f}".format(api['data'][i]['quote']['USD']['price']), bg="light grey", fg="black", font=("Arial Bold", 10), padx="5", pady="5", borderwidth=2, relief="groove")
                price.grid(row=c, column=1, sticky=N+S+E+W)

                no_of_coins = Label(pycrypto, text=coin["no_of_coins"], bg="light grey", fg="black", font=("Arial Bold", 10), padx="5", pady="5", borderwidth=2, relief="groove")
                no_of_coins.grid(row=c, column=2, sticky=N+S+E+W)

                amount_paid = Label(pycrypto, text="${0:0.2f}".format(total_paid), bg="light grey", fg="black", font=("Arial Bold", 10), padx="5", pady="5", borderwidth=2, relief="groove")
                amount_paid.grid(row=c, column=3, sticky=N+S+E+W)

                curr_val = Label(pycrypto, text="${0:0.2f}".format(current_price), bg="light grey", fg="black", font=("Arial Bold", 10), padx="5", pady="5", borderwidth=2, relief="groove")
                curr_val.grid(row=c, column=4, sticky=N+S+E+W)

                pl_coin = Label(pycrypto, text="${0:0.2f}".format(pl_per_coin), bg="light grey", fg=font_color(float("{0:0.2f}".format(pl_per_coin))), font=("Arial Bold", 10), padx="5", pady="5", borderwidth=2, relief="groove")
                pl_coin.grid(row=c, column=5, sticky=N+S+E+W)

                pl_amount = Label(pycrypto, text="${0:0.2f}".format(pl_amount), bg="light grey", fg=font_color(float("{0:0.2f}".format(pl_amount))), font=("Arial Bold", 10), padx="5", pady="5", borderwidth=2, relief="groove")
                pl_amount.grid(row=c, column=6, sticky=N+S+E+W)

                c+=1

    total_amount_paid = Label(pycrypto, text=int(total_amount_paid), bg="white", fg="blue", font=("Arial Bold", 10),
                              padx="5",
                              pady="5", borderwidth=2, relief="groove")
    total_amount_paid.grid(row=c, column=3, sticky=N + S + E + W)


    total_curr = Label(pycrypto, text=int(total_curr), bg="white", fg="blue", font=("Arial Bold", 10), padx="5", pady="5",
                       borderwidth=2, relief="groove")
    total_curr.grid(row=c, column=4, sticky=N + S + E + W)

    net_pl_amount = Label(pycrypto, text=int(net_pl_amount), bg="white", fg=font_color(float("{0:0.2f}".format(net_pl_amount))), font=("Arial Bold", 10), padx="5",
                          pady="5", borderwidth=2, relief="groove")
    net_pl_amount.grid(row=c, column=6, sticky=N + S + E + W)

    api = ""

    update = Button(pycrypto, text="UPDATE", bg="white", fg="blue",command=my_portfolio, font=("Arial Bold", 10), borderwidth=2, relief="groove")
    update.grid(row=c+1, column=6, sticky=N + S + E + W)

    print("And hence the net amount for portfolio is ", net_pl_amount)


name = Label(pycrypto, text="Coin Name", bg="dark blue", fg="white", font=("Arial Bold", 10), padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycrypto, text="Price", bg="dark blue", fg="white", font=("Arial Bold", 10),padx="5", pady="5", borderwidth=2, relief="groove")
price.grid(row=0, column=1, sticky=N+S+E+W)

no_of_coins = Label(pycrypto, text="coins owned", bg="dark blue", fg="white", font=("Arial Bold", 10),padx="5", pady="5", borderwidth=2, relief="groove")
no_of_coins.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pycrypto, text="Total amount paid",bg="dark blue", fg="white", font=("Arial Bold", 10),padx="5", pady="5", borderwidth=2, relief="groove")
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

curr_val = Label(pycrypto, text="Current Value", bg="dark blue", fg="white", font=("Arial Bold", 10),padx="5", pady="5", borderwidth=2, relief="groove")
curr_val.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(pycrypto, text="P/L per coin", bg="dark blue", fg="white", font=("Arial Bold", 10), padx="5", pady="5", borderwidth=2, relief="groove")
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

total_pl = Label(pycrypto, text="Total P/L with coin", bg="dark blue", fg="white", font=("Arial Bold", 10), padx="5", pady="5", borderwidth=2, relief="groove")
total_pl.grid(row=0, column=6, sticky=N+S+E+W)

my_portfolio()

pycrypto.mainloop()
print("program completed")