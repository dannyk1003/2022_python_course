from sys import argv

number = int(argv[1])

print(argv[0])
print(100/number)

'''
python TestExcept.py
IndexError: list index out of range

python TestExcept.py abc
ValueError: invalid literal for int() with base 10: 'abc'

python TestExcept.py 0
ZeroDivisionError: division by zero
'''
