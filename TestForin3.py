text = 'Hello!!!'
nums = range(len(text))
print(zip(nums , text))
print(list(zip(nums , text)))

for n,t in list(zip(nums,text)): # zip(a,b) -> combine 2 same len data
    print(n,t)

nn = [10,20,30]
a,b,c = nn
print(a)


print(list(zip(('a','b','c') , (1,2,3))))
print(list(zip(('a','b','c') , (1,2,3)))[1])

for n,t in zip(range(len(text)),text):
    print(n,t)