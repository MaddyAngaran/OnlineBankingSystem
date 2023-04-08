import unittest
from main import *

# Add imports here
from Account import *
from Bank import *
from GUI import *
from User import *

class UnitTests(unittest.TestCase):

  def test_addInterest(self):
      # Enter code here
      person1 = Bank.create_user("Jill", "greg@gmail.com", "1234567890", "jack123")
      person1.create_account("Savings")
      person1Account = person1.get_account()
      person1Account.deposit(100)
      person1Account.addInterest()
      self.assertEquals(person1Account.get_balance(), 101)

  def test_withdraw(self):
      # Enter code here
      person1 = Bank.create_user("Jack", "greg@gmail.com", "1234567890", "jack123")
      person1.create_account("Chequing")
      person1Account = person1.get_account()
      person1Account.deposit(100)
      person1Account.withdraw(50)
      self.assertEquals(person1Account.get_balance(), 50)

  def test_deposit(self):
      # Enter code here
      person1 = Bank.create_user("Jack", "greg@gmail.com", "1234567890", "jack123")
      person1.create_account("Chequing")
      acc = person1.get_account()
      acc.deposit(100)
      self.assertEquals(100, acc.get_balance())

  def test_login(self):
      # Enter code here
      person1 = Bank.create_user("Greg", "greg@gmail.com", "1234567890", "greg123")
      person1Id = person1.get_user("Greg")
      person1Id == Bank.get_user(person1Id)
      self.assertEquals(person1Id, Bank.login(person1Id, "greg123"))

  def test_accountNumber(self):
      # Enter code here
      person1 = Bank.create_user("John", "john@gmail.com", "1234567890", "john123")
      person1Id = person1.get_user("John")
      person1.create_account("Chequing")
      person1Account = person1.get_account()
      self.assertEquals(person1Account[0], person1.get_account(person1Account[0]))

  def test_createUser(self):
      # Enter code here
      person1 = Bank.create_user("Greg", "greg@gmail.com", "1234567890", "greg123")
      person1Id = person1.get_user("Greg")
      self.assertEquals(person1Id,Bank.get_user(person1Id))

