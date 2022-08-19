from bank3 import Account, account
acct = Account('Cand', '00123-4560002', 50)
#acct_name = Account('Cand', '00123-4560002', 50).my_name()

#acct : 物件 Account : 類別
print(acct)
print(int(acct))
#print(acct.balance)

acct.pi = 3.14159
print(acct.pi)
print(acct.balance)
#print(int(acct))
#print('balance = ',int(acct))
#print(abc(acct))

# acct.__balance = 0
print(acct)

def hello():
    print('Hello!')

acct.hello = hello
acct.hello()

def hello2():
    return 'Hello2'

acct.hello2 = hello2
print(acct.hello2())

bcct = Account('Cand', '00123-4560002', 5555)

def hello555(balance):
    return f'balance + {balance}'


bcct.hello555 = hello555
print(bcct.hello555(bcct.balance))
