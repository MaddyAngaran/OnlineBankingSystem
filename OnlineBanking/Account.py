import pickle

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

class ChequingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        self.type = "Chequing Account"

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit < amount:
            return False
        self.balance -= amount
        return True


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
        self.type = "Savings Account"

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance = self.balance + interest

    def get_user(self, name):
        if name not in self.users:
            raise ValueError("User not found")
        return self.users[name]

    def load_users(self):
        try:
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.users, f)
