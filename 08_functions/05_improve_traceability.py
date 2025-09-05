""""IMPROVING TRACEABILITY.

Your shop adds a 10% VAT on every order.

You want this to be consistent and traceable.

Task:
    1. Write add_vat(price, vat_rate)
    2. Use it to compute final prices for 3 orders."""


def add_vat(price, vat_rate):
    return round(price * (1+(vat_rate/100)),2)

orders = [100, 150, 200]

final_prices=[]
for price in orders:
    final_prices.append(add_vat(price, 12))

print(final_prices)