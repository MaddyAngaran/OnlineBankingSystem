from Account import SavingsAccount, ChequingAccount
import pickle
import random


class User:
    def __init__(self, userId, name, email, phoneNumber, filename, password):
        self.userId = userId
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.filename = filename
        self.accounts = self.load_accounts()
        self.password = password

    def create_account(self, account_type, initial_balance=0):
        account_number = random.randrange(100000, 1000000)
        while account_number in self.accounts:
            account_number = random.randrange(100000, 1000000)
            print(account_number)
        if account_type == 'Chequing':
            account = ChequingAccount(account_number, initial_balance)
        elif account_type == 'Savings':
            account = SavingsAccount(account_number, initial_balance)
        else:
            raise ValueError("Invalid account type")
        self.accounts[account_number] = account
        self.save_accounts()
        print(self.accounts[account_number])
        return account
    
    def get_userId(self):
      return self.userId

    def get_account_info(self):
        account_info = []
        for account_number, account in self.accounts.items():
            account_type = type(account).__name__
            balance = account.get_balance()
            account_info.append((account_number, account_type, balance))
        return account_info

    def get_account(self, account_number):
        if int(account_number) not in self.accounts:
            raise ValueError("Account number not found")
        return self.accounts[int(account_number)]

    def load_accounts(self):
        try:
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {}

    def save_accounts(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.accounts, f)

    def deposit(self, amount, account_number):
        account = self.get_account(account_number)
        account.deposit(amount)
        self.save_accounts()

    def withdraw(self, amount, account_number):
        account = self.get_account(account_number)
        account.withdraw(amount)
        self.save_accounts()
