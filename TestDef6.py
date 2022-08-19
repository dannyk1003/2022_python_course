def sum123(a,b,c):
    return a+b+c

data = {'a':10,'b':20,'c':30}
print(sum123(*data))
print(sum123(**data))

'''
*data接收任意數量的位置型參數  
**data接收任意數量的關鍵字參數
'''