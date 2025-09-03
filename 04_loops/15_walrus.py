"""Understood the usage of walrus operator"""

value = 10
remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is :{remainder}")

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")
else:
    print(f"Perfectly divisible")