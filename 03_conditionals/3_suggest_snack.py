"""A local cafe wants a program that suggests a snack.
If a customer asks for cookies or a samosa, it confirms the order.
Otherwise it says, it's not available.

Task:
Take snack input.
If it's 'cookies' or 'samosa', confirm the order.
Else, show unavailability"""

customer_name = input("Hello!! Thanks for choosing us. May I have your name please?: ")

customer_input = input(f"Thanks {customer_name}! What would you like to have? : \n").lower()

if customer_input in ('cookies', 'samosa'):
    print("Order confirmed!! Please have a seat while we prepare your order.")
else:
    print(f"Sorry {customer_name}. We only serve cookies or samosa")