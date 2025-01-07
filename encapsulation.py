class BankAccount:
    def __init__(self, name):
        self._balance = 0
        self.name = name
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        self._balance -= amount
    def get_balance(self):
        return self._balance
    def __str__(self):
        return f"Name: {self.name} and Balance: Hidden"
    #using encapsulation
ruman = BankAccount("Ruman")
ruman.deposit(100)
print(ruman)
print(ruman.get_balance()) # output: 100
ruman.withdraw(50) # output: 50
ruman.deposit(400) #output: 450
ruman.withdraw(100)#output: 350
print(ruman.get_balance())