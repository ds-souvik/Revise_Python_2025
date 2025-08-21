"""Creating a Food Menu board.
Each item must be numbered.
Task:
    1. Use enumerate() to print menu items with numbers."""

item_input = input(f"Please mention the menu items: ").split(",")

print(list(enumerate(item_input, start=1)))

for index, value in enumerate(item_input, start=1):
    print(f"{index}. {value.strip().capitalize()}")

