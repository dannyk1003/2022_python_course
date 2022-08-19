import shelve
s = shelve.open('data.shelve')
s['A'] = [10,20,30]
s['B'] = [40,50,60]
print(s['A'])
print(s['B'])
s.close