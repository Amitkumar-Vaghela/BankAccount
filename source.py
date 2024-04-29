import random

class Client:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    
    def generate_account_number(self):
        return ''.join(str(random.randint(0, 9)) for _ in range(8))
    
    def create_account(self, client):
        account_number = self.generate_account_number()
        if account_number not in self.accounts:
            self.accounts[account_number] = {'client': client, 'account': Account(account_number)}
            print(f"Account {account_number} created for client {client.name}.")
        else:
            print("An error occurred while creating the account.")
    
    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['account']
        else:
            print("Account not found.")
            return None

# Function to get user input for creating a client
def get_client_info():
    name = input("Enter client's name: ")
    address = input("Enter client's address: ")
    return Client(name, address)

# Function to get user input for account operations
def perform_account_operations(account):
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Example usage:
bank_name = input("Enter bank name: ")
bank = Bank(bank_name)
client_info = get_client_info()
bank.create_account(client_info)
account_number = input("Enter account number: ")
account = bank.get_account(account_number)
if account:
    perform_account_operations(account)
