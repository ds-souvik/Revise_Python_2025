"""You're managing a busy tea stall.
You receive many orders and want to print each customer's name along with the type of chai they ordered.

Task:
    1. Write a function print_order(name, chai_type)
    2. Call it multiple times for different customers."""

def print_order(name, chai_type): #variables here are called parameters
    #check if the variables are populated and if the variables are of string datatype
    if name and chai_type and isinstance(name, str) and isinstance(chai_type, str):
        return f"{name} ordered {chai_type}"
    else:
        return "Incomplete order"

print(print_order("Souvik", "Ginger tea")) #variables here are called arguments
print(print_order("", "Lemon team"))
print(print_order(123, "Ginger tea"))