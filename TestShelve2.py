import shelve
s = shelve.open('data.shelve')
s['C'] = [70,80,90]
print(s['A'])
print(s['B'])
print(s['C'])
s.close() # save file