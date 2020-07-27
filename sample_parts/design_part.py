from sample_parts.program1 import *

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")


name = Label(pycrypto, text="Coin Name", bg="grey", fg="white", font=("Arial Bold", 10))
name.grid(row=0, column=0)

price = Label(pycrypto, text="Price", bg="black", fg="white", font=("Arial Bold", 10))
price.grid(row=0, column=1)

no_of_coins = Label(pycrypto, text="coins owned", bg="grey", fg="white", font=("Arial Bold", 10))
no_of_coins.grid(row=0, column=2)

amount_paid = Label(pycrypto, text="Total amount paid", bg="black", fg="white", font=("Arial Bold", 10))
amount_paid.grid(row=0, column=3)

curr_val = Label(pycrypto, text="Current Value", bg="grey", fg="white", font=("Arial Bold", 10))
curr_val.grid(row=0, column=4)

pl_coin = Label(pycrypto, text="P/L per coin", bg="black", fg="white", font=("Arial Bold", 10))
pl_coin.grid(row=0, column=5)

total_pl = Label(pycrypto, text="Total P/L with coin", bg="grey", fg="white", font=("Arial Bold", 10))
total_pl.grid(row=0, column=6)


pycrypto.mainloop()
print("program completed")