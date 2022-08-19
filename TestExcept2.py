from sys import argv

try:
    number = int(argv[1])
    print(100 / number)
except IndexError as ie:
    print('enter number')
    print(ie)
except ValueError as ve:
    print('enter int')
except ZeroDivisionError as ze:
    print('dont enter 0')
finally:
    print('must happend')

