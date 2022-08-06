def number():
    checker = 0
    while checker != 1:
        x = input("enter number:")
        checker = 0
        for i in x:
            if i not in str(list(range(10))):
                print("not a number!")
                break
            else:
                checker += 1
        if checker == len(x):
            checker = 1  
    return int(x)


def counter():
    x = number()

    while True:
        y = input("enter operator:")
        if y == "+":
            break
        elif y == "-":
            break
        elif y == "*":
            break
        elif y == "/":
            break
        elif y == "**":
            break
        else:
            print("not a operator!")
        
    z = number()

    if y == "+":
        answer = x + z
    elif y == "-":
        answer = x - z
    elif y == "*":
        answer = x * z
    elif y == "/":
        answer = x / z
    elif y == "**":
        answer = x ** z
    else:
        answer = "Error"

    print(f"{x} {y} {z} = {answer}")
    

"""
switch y:
    case "+":
        answer = x + z
    case "-":
        answer = x - z
    case "*":
        answer = x * z
    case "/":
        answer = x / z
"""

index = 0
while True:
    counter()

    while True:
        index = input("countinue?(Y/N):")
        #print(index)
        #print(index == "N")


        if index.upper() == "N":
            print("good bye!")
            break
        elif index.upper() == "Y":
            break
        else:
            print("plz type again~")
    if index.upper() == "Y":
        continue
    break


        

