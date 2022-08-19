#number = int(input('enter number: '))

while  True:
    try:
        print('1. ' , 100 / int(input('enter number: ')))
        break
    except ValueError as ve:
        print('3. ValueError')
    except ZeroDivisionError as ze:
        print('4. ZeroDivisionError')
    finally:
        print('5. must happend')
    print('6. controll')
print('7. outside!')

'''
from sys import argv
try:
    number = 100/int(argv[1])
    print('1.程式順利執行')
except IndexError as ie:
    print('2.程式發生例外1')
except ValueError as ve:
    print('3.程式發生例外2')
finally:
    print('4.一定會發生')
print('5.程式受控制')
'''