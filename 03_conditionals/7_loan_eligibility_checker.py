"""Loan Eligibility Checker: Write a function as part of coding exercise
You’re building a basic loan eligibility checker for a bank. A customer must meet two conditions to be eligible:

Tasks:
1. If the user’s age is 21 or above, check:
    a. If income is 25,000 Bucks or above, return: "Eligible for loan".
    b. Otherwise, return: "Not eligible: Income too low".
2. If the user’s age is less than 21, return: 'Not eligible: Age must be 21 or above' """

# This function will be tested by the evaluation system. Do not modify the function name or parameters.
def check_loan_eligibility(age: int, income: float) -> str:
    # Write your code below this line
    if age >= 21:
        if income >=25000:
            return "Eligible for loan"
        else:
            return "Not eligible: Income too low"
    else:
        return "Not eligible: Age must be 21 or above"