""" DELIVERY FEES WAIVER SYSTEM:
You run an online tea store. 
If the order amount is more than 300 rs:
    Delivery is free
Otherwise:
    It costs 30 rs.

Task:
1. Input order amount
2. Use ternary operator to decide delivery fee
"""
#ternary operator
order_input = int(input("Order amount: "))
print(f"{'Congratulations! Free Delivery' if order_input > 300 
         else ('Sorry, Invalid input. Please try again' 
               if order_input < 0 else 'Delivery charges: 30 rs')}")