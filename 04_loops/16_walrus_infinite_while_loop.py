"""Walrus plus infinit while loop"""

available_furniture = dict([("sofa", 40000), ("bed", 60000), ("cupboard", 18000), ("table", 12000)])
print(f"Available stocl at the store: {available_furniture}")


while (cust_choice := input("What do you want to buy from us: ").lower()) not in available_furniture.keys():
    print(f"""Sorry {cust_choice.capitalize()} not available at the store. Please select from the above mentioned list""")

print(f"Please proceed to pay ${available_furniture[cust_choice]} for the {cust_choice.capitalize()}")