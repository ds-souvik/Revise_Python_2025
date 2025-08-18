"""Food Menu Selector
You’re creating a menu price lookup system for a digital food ordering app using the match-case statement.

Tasks:
1. Define a function get_item_price that takes a string input item.
2. Use match-case to return the following based on the item name:
    1. "pizza" → "Price: 30 bucks" 
    2. "burger" → "Price: 15 bucks" 
    3. "pasta" → "Price: 20 bucks"
    4. "salad" → "Price: 10 bucks"
    5. Any other item → "Item not available"
Make sure the item check is case-insensitive (e.g., “BURGER” or “burger” should both match).
"""

# This function will be tested automatically. 
# Do not change the function name or parameter type.
def get_item_price(item: str) -> str:
    # write your code below this line
    match item.lower():
        case "pizza":
            return "Price: 30 bucks"
        case "burger":
            return "Price: 15 bucks"
        case "pasta":
            return "Price: 20 bucks"
        case "salad":
            return "Price: 10 bucks"
        case _:
            return "Item not available"