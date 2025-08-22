"""You're preparing an order summary with customer names and their total bill.
Task:
    1. Use 2 lists: one for the names and one for the bills.
    Print: "[Name] paid rs[amount]"""

customer_names = input("Mention the customer names: ").split(",")
customer_bill = str(input("Mention the customer bills: ")).split(",")

if len(customer_names) != len(customer_bill):
    print(f"The list of names and bill are not matching. Please check the upstream system!")
else:
    for val in range(len(customer_bill)):
        print(f"{customer_names[val].strip().capitalize()} paid rs {customer_bill[val].strip()} ")

print("Now same task using zip()")
'''Using zip()'''

if len(customer_names) == len(customer_bill):
    for item in zip(customer_names, customer_bill, strict = True):
        print(f"{item[0].strip().capitalize()} paid rs {item[1].strip()}")
else:
    print("The list of names and bill are not matching. Please check the upstream system!")

print("zip() using key, value pair")
if len(customer_names) == len(customer_bill):
    for name, amount in zip(customer_names, customer_bill, strict=True):
        print(f"{name.strip().capitalize()} paid rs {amount.strip()}")
else:
    print("The list of names and bill are not matching. Please check the upstream system!")
