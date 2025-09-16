class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance 
  
  def deposit(self, amount): 
    amount = int(amount)
    self.balance += amount
    return self.balance
  
  def withdraw(self, amount):
    amount = int(amount)
    self.balance -= amount
    return self.balance

  def display_balance(self):
    return self.balance

account = BankAccount("John", "Doe", "123456", "Checking", "1234", 100)
account.deposit(96)
account.withdraw(25)
print(account.display_balance())