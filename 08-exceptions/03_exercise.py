# Mini Project: ATM Simulator
# Features
# Check balance
# Deposit money
# Withdraw money
# Exit

# Exceptions to Handle
# User enters text instead of a number → ValueError
# Withdraw amount greater than balance → Custom Exception
# Negative deposit/withdraw amount → ValueError
# Division by zero (optional statistics feature)
# Unexpected errors → Generic Exception

balance = 5000

class InsufficientBalanceError(Exception):
    pass

print("Welcome to ATM! \n 1)Check balance \n 2)Deposit money \n 3)Withdraw money")

choice = int(input("Enter your action : "))

def deposit_money(balance, amount):
    
    try:
        if amount < 0:
            raise ValueError("Invalid amount")
        balance += amount
        return balance
    except Exception as e:
        print("Error : ", e)
        

def withdraw_money(amount):
    balance = 5000
    try:
        if amount > balance:
            raise InsufficientBalanceError("Insufficient Balance")
        elif type(amount) == str:
            raise TypeError("Invalid amount")
        balance -= amount
        return balance
    except Exception as e:
        print("Error : ", e)
        
if choice == 1:
    balance = 5000
    print(f"Balance : {balance}")
    
elif choice == 2:
    amount = int(input("Enter the amount to deposit : "))
    new_balance = deposit_money(amount)
    print(f"New Balance : {new_balance}")
    
elif choice == 3:
    amount = int(input("Enter the amount to withdraw : "))
    new_balance = withdraw_money(amount)
    print(f"Amount withdrawn : {amount}")
    print(f"New Balance : {new_balance}")
else:
    raise ValueError("Action does not exist")