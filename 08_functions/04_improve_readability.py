"""IMPROVING READABILITY

YOU SELL DIFFERENT CHAI SIZES.
INSTEAD OF WRITING FORMUALS EVERYWHERE, CREATE A FUNCTION.

TASKS:
    1. Write calculate_bills(cups, proce_per_cup)
    2. Return total bill.
    3. Use this function for multiple orders."""

def calculate_bills(cups, price_per_cup):
    return f"Your total bill amount is {cups * price_per_cup}"

print(calculate_bills(4, 15))

