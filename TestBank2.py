from bank2 import Account

acct = Account('Alan', '00123-4560000', 10000)
acct.deposit(1000)
print(acct)

acct2 = Account('Bob', '00123-4560001', 100)
acct2.deposit(10)
print(acct2)