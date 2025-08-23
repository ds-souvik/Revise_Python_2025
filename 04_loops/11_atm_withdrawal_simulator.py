"""ATM Withdrawal Simulator
Imagine you’re building a backend feature for an ATM. Customers can request multiple 
withdrawals during one session. Your task is to simulate how the system should handle 
each request based on the account balance.
Tasks:
    1. Use a while loop to iterate through the list named withdrawals. 
    2. For every withdrawal: 
        ✅ If the current balance is enough: 
            Subtract the amount. 
            Append a success message: "Withdrawn: {amount}" 
        ❌ If not enough: 
            Append a message: "Insufficient funds for requested amount: {amount}"
    3. After all withdrawals: 
        Append the final balance as: "Remaining Balance: balance" 
    4. Return a list containing all the messages."""

# This function will be tested automatically. 
# Do not change the function name or parameters.
def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    # Write your code below this line
    counter=0
    withdrawal_result=[]
    while counter < len(withdrawals):
        if balance >= withdrawals[counter]:
            withdrawal_result.append(f"Withdrawn: {withdrawals[counter]}")
            balance -= withdrawals[counter]
            counter += 1
        else:
            withdrawal_result.append(f"Insufficient funds for requested amount: {withdrawals[counter]}")
            counter += 1
    
    withdrawal_result.append(f"Remaining Balance: {balance}")
    
    return withdrawal_result

print(f"{simulate_atm_withdrawals(100000, [1000, 7000, 1, 999, 50000])}")