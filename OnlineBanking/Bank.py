import pickle
from User import User
import random

class Bank:
    def __init__(self, filename):
        self.filename = filename
        self.users = self.load_users()
        self.current_user = None

    def create_user(self, name, email, phoneNumber, password):
        userId = random.randrange(100000, 1000000)
        while userId in self.users:
          userId = random.randrange(100000, 1000000)
          print(userId)
        user = User(userId, name, email, phoneNumber, self.filename + '_' + str(userId) + '.dat', password)
        self.users[userId] = user
        self.save_users()
        return user

    def login(self, userId, password):
        user = self.get_user(userId)
        if user is not None and user.password == password:
            return user
        else:
            return None      

    def get_user(self, userId):
        if int(userId) not in self.users:
            raise ValueError("User not found")
        return self.users[int(userId)]

    def load_users(self):
        try:
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.users, f)

