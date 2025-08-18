"""Age Verification System
You’re building a system to verify user age for access.
Tasks:
1. Define a function verify_age that accepts a string input named age_str.
2. Convert age_str to an integer using int().
3. Use a ternary operator to return: 
    'Access Granted' if age is 18 or older
    'Access Denied' otherwise"""

# This function will be tested automatically. 
# Do not change the function name or parameter type.
def verify_age(age_str: str) -> str:
    # Write your code here
    return "Access Granted" if int(age_str) >=18 else("Invalid Input" if int(age_str) < 0 else "Access Denied")

