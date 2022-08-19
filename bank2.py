class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def __str__(self):
        #return '<Account:{}, {}, {}>'.format(self.name, self.number, self.balance)
        return f'<Account:{self.name}, {self.number}, {self.balance}>'
