"""You receive a list of name for chai orders.
The goal is to print out the order queue.
Task:
    1. Use a list of names.
    2. Print: "order ready for [name]"""

customer_names_in_batch = input("Please enter the customer names in the queue: ").split(",")

for name in customer_names_in_batch:
    print(f"Order ready for {name.strip().capitalize()}")