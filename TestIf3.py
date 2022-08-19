score = int(input('plz enter score : '))
while score <1 or score > 100:
    print('enter again!')
    score = int(input('plz enter score : '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')


'''
score = input('plz enter score : ') # str vs str
if score >= '90':
    print('A')
elif score >= '80':
    print('B')
elif score >= '70':
    print('C')
elif score >= '60':
    print('D')
else:
    print('F')


score = int(input('plz enter score : ')) # only one time
if score < 1 or score > 100:
    print('enter again!')
elif score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
'''