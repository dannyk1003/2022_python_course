import bank

acct = bank.account('Alan','00123-4560000',10000)
bank.deposit(acct,100)
print(bank.desc(acct))

acct2 = bank.account(' Bob','00123-4560001',10000)
bank.deposit(acct2,100)
print(bank.desc(acct2))
