class Account:
    #Constructor 建構子
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
    
    def __str__(self): # return information
        #return 'do nothing...'
        return f'Account({self.name},{self.number},{self.balance})'
        #return f'Account({name},{number},{balance})'

    def __repr__(self):
        return f'Account({self.name},{self.number},{self.balance})'

    def __int__(self):
        return self.balance

    def my_name(self):
        return self.name


def account(name, number, balance):
    return f'Account({name},{number},{balance})'