# You’re building a basic loan eligibility checker for a bank.
# A customer must meet two conditions to be eligible:

# Tasks:
# If the user’s age is 21 or above, check:
# If income is 25,000 Bucks or above, return: "Eligible for loan"
# Otherwise, return: "Not eligible: Income too low"
# If the user’s age is less than 21, return: "Not eligible: Age must be 21 or above"

age = int(input("Enter your age : "))
income = int(input("Enter your income : "))

if age >= 21 : 
    if income >= 25000 :
        print("Eligible for loan")
    else : 
        print("Not eligible: Income too low")
else : 
    print("Not eligible: Age must be 21 or above")
    