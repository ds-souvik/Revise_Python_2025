"""Generate Multiplication Table
You are developing a feature in an educational app that displays multiplication tables.
Tasks:
    1. Write a function named multiplication_table that takes a single integer argument number. 
    2. Using a for loop and range(), generate the multiplication table for number from 1 to 10. 
    3. Return a list of strings in the following format: 
        "number x i = result" 
        (Example: "3 x 4 = 12")
"""

# This function will be tested automatically. 
# Do not change the function name or parameter type.
def multiplication_table(number: int) -> list[str]:
    # Write your code below this line
    table=[]
    for factor in range(1,11):
        multiple = number * factor
        table.append(f"{number} x {factor} = {multiple}")
    
    return table