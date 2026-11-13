class BankAccount:

  def __init__(self, account_number, holder_name, initial_balance=0.0):
    self.account_number = account_number
    self.holder_name = holder_name
    self.balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
    return "Deposit amount must be positive."

  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
    return "Invalid withdrawal amount or insufficient funds."

  def get_balance(self):
    return f"Account Holder: {self.holder_name} | Balance: ${self.balance:.2f}"