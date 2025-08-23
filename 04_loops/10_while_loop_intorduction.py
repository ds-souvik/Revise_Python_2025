"""Learn usage of WHILE loop.
You want to simulate tea heating. It starts at 40 degrees C and boils at 100 degrees C.
Task:
    1. Use a while loop.
    2. Increase temperature by 15 until it reaches or exceeds 100
    3. Print each temperature step."""

tea_temp = 40

while tea_temp < 100:
    print(f"Team temperature is {tea_temp}")
    tea_temp += 15

print("Tea is ready to boil")