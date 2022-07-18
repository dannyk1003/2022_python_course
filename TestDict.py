acct = {'Test1':1234, 'Test2':2234}
print(acct)
print(type(acct))

print(acct['Test1'])
print(acct['Test2'])

acct.update({'Test3':3234}) # add to dict
print(acct)

acct['Test4'] = 4234 # add to dict
print(acct)

del acct['Test1']
print(acct)
print('Test1' in acct)
print(acct.get('Test1'))

acct.update({'Test5':5234, 'Test6':6234})
print(acct)


keys_to_remove = ['Test5', 'Test6'] # use loop to remove multiple keys
for key in keys_to_remove:
    del acct[key]
print(acct)
