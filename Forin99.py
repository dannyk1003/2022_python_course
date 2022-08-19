'''
for x in range(2,10):
    for y in range(1,10):
        print(x , '*' , y , '=' , x*y , end='  ',sep='')
    print()
'''

a,b = [2,1]
while a <= 9:
    b = 1
    while b <= 9:
        print(a , '*' , b , '=' , a*b , end='  ',sep='')
        b = b+1
    print()
    a = a+1