DataA = {'A','B','c','d'}
DataB = {'e','f','A','B'}
DataC = {'A','e'}

print('inner join : ' , DataA & DataB) # & = and
print('A-(A&B) : ' , DataA - DataB)
print('A,B union : ' , DataA | DataB) # | = or
print('A|B - A&B : ' , DataA ^ DataB) # ^ = XOR
print('A|B - A&B : ' , (DataA | DataB) - (DataA & DataB))
print('DataB > DataC : ' , DataB > DataC)