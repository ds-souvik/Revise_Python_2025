"""A tea stall offers different prices for different cup sizes. Write a program that calculates 
the price based on size. 

Task: 
    1. Input 'small', 'medium' and 'large'.
    2. Small = 10 rs, Medium = 15 rs and Large = 20 rs.
    3. If invalid: show 'Unknown cup size'."""

import time

'''Testing execution time for both the ways'''

#Get the current UTC time
start_time = time.time()

tea_price = dict(cutting = 8, small = 10, medium = 15, large = 20)

def calculate_price(tea_size):
    if tea_size in tea_price:
        return f"{customer_name}, Please pay {tea_price[tea_size]}"
    else:
        return f"Sorry {customer_name}. Unknown cup size"

customer_name = input("Hello, Welcome to Chaayos!! May I have your name please?: ")

customer_order_input = input(f"Hey {customer_name}! Choose your cup size: (Cutting/ Small/ Medium/ Large) : \n").lower()

print(calculate_price(customer_order_input))
print(time.time() - start_time)

#--------------------------------------------------------
start_time = time.time()
customer_name = input("Hello, Welcome to Chaayos!! May I have your name please?: ")
customer_order_input = input(f"Hey {customer_name}! Choose your cup size: (Cutting/ Small/ Medium/ Large) : \n").lower()

if customer_order_input == 'cutting':
    print(f"{customer_name}, Please pay rs 10")
elif customer_order_input == 'small':
    print(f"{customer_name}, Please pay rs 10")
elif customer_order_input == 'medium':
    print(f"{customer_name}, Please pay rs 15")
elif customer_order_input == 'large':
    print(f"{customer_name}, Please pay rs 20")
else:
    print(f"Sorry {customer_name}. Unknown cup size")

print(time.time() - start_time)