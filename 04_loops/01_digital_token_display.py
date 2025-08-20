"""Digital Token display


A tea stall owner has a digital token display.
For every customer in line, a token number is printed and chai is served.
Task:
    1. Use a for loop to generate token numbers from 1 to 10 using range()
    2. Print: Serving chai to Token #[number]"""

for token in range(1,11):
    print(f"Serving chai to token #{token}")