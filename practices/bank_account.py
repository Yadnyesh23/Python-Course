# Bank Management System
import json


class InvalidAmountError(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class AccountAlreadyExistError(Exception):
    pass

class AccountDoesNotExist(Exception):
    pass

class Account:
    
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 10000
    
    def deposit(self, amount):
        if amount <= 0 :
            raise InvalidAmountError("Invalid amount. Please enter amount greater than 0.")
        self.balance += amount
        return f"Amount deposited : {amount}. New Balance : {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalance(f"Insufficient Balance. Current balance : {self.balance}")
        if amount <= 0:
            raise InvalidAmountError(
                 "Amount must be greater than 0"
           )
        self.balance = self.balance - amount
        return f"Amount withdrawn : {amount}. New Balance : {self.balance}"
    
    def display_details(self):
        return f"-----Account Details----- \nAccount number : {self.account_number} \nAccount Holder : {self.account_holder} \nBalance : {self.balance}"


class Bank:
    
    def __init__(self):
        self.accounts = []
    
    def accountExist(self, account_number) :  
        for existing_account in self.accounts:
            if existing_account.account_number == account_number:
                return True
        return False
        
    def add_account(self, account):
        for existing_account in self.accounts:
            if account.account_number == existing_account.account_number:
                raise AccountAlreadyExistError("Account already exist!")
        self.accounts.append(account)
        return f"Account with acc_no {account.account_number} has been added"
    
    def close_account(self, account_number):
        for existing_account in self.accounts:
            if account_number == existing_account.account_number:
                self.accounts.remove(existing_account)
                return f"Account with acc_no {account_number} has been removed"
        raise AccountDoesNotExist("Account does not exist")
    
    def display_accounts(self):
        for account in self.accounts:
            print(account.display_details()) 
     
    def search_account(self, account_number):
        for existing_account in self.accounts:
            if existing_account.account_number == account_number:
                return existing_account.display_details()
        raise AccountDoesNotExist("Account does not exist")
    
    def deposit_money(self, account_number , amount):
        for existing_account in self.accounts:
            if existing_account.account_number == account_number:
                return existing_account.deposit(amount)
        raise AccountDoesNotExist("Account does not exist.")
                
    def withdraw_money(self, account_number , amount):
        for existing_account in self.accounts:
            if existing_account.account_number == account_number:
                return existing_account.withdraw(amount)
        raise AccountDoesNotExist("Account does not exist.")
    
    def transfer_money(self, sender, reciever, amount):
        if self.accountExist(sender.account_number) and self.accountExist(reciever.account_number):
            sender.withdraw(amount)
            reciever.deposit(amount)
            return f" Account number : {sender.account_number} sent rupees {amount} to account number {reciever.account_number}"
        raise AccountDoesNotExist("Accounts does not exist!")
    
    def save_data(self):
        
        data = []
        
        for account in self.accounts:
            data.append({
                "Account Number" : account.account_number,
                "Account Holder" : account.account_holder,
                "Balance" : account.balance
            })
        
        with open('bank_account.json', "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved succesfully!")
    
    def load_data(self):
        with open("bank_account.json", "r") as file:
            account_data = json.load(file)
        
        self.accounts = []
        for account in account_data:
            new_account = Account(
                account["account_number"],
                account["account_holder"],
                account["balance"],
            )
        
        self.accounts.append(new_account)


bank = Bank()

account1 = Account(12345, "Yadnyesh")
account2 = Account(12346, "Kevin")
account3 = Account(12347, "Suneet")

print(bank.add_account(account1))
print(bank.add_account(account2))
print(bank.add_account(account3))

print(bank.save_data())
