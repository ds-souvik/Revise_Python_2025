"""Delivery Charge Calculator
You’re building a delivery system for an e-commerce platform. Depending on the distance of the customer’s address, different delivery charges apply.

Tasks:
1. Take input from the user for delivery distance in Kilometers and store it in a variable named distance.
2. If the distance is 2 km or less, return the string: "Delivery charge: 0"
3. If the distance is greater than 2 km but not more than 5 km, return the string: "Delivery charge: 30"
4. If the distance is greater than 5 km but not more than 10 km, return the string: "Delivery charge: 50"
5. If the distance is more than 10 km, return the string: 'Delivery not available for your location.' 
"""

# This function will be tested automatically. 
# Do not change the function name or parameter type.
def calculate_delivery_charge(distance: float) -> str:
    # Write your code below this line
    if distance > 0 and distance <= 2:
        return "Delivery charge: 0"
    elif distance > 2 and distance <= 5:
        return "Delivery charge: 30"
    elif distance > 5 and distance <= 10:
        return "Delivery charge: 50"
    elif distance > 10:
        return "Delivery not available for your location."
    else:
        return "Invalid input"

distance = int(input("Hello, please provide the distance in Kms: "))
print(calculate_delivery_charge(distance))