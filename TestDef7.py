def some(*arg1, **arg2):
    print('arg1 = ' , arg1)
    print('arg2 = ' , arg2)

some(10,20,30)
some(a=10,b=20,c=30)


'''
*data接收任意數量的位置型參數  
**data接收任意數量的關鍵字參數
'''