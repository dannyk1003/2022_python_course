
def counter():
    x = int(input("enter first number:"))

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
        else:
            print("not a operator!")
        
    z = int(input("enter second number:"))

    if y == "+":
        answer = x + z
    elif y == "-":
        answer = x - z
    elif y == "*":
        answer = x * z
    elif y == "/":
        answer = x / z
    else:
        answer = "Error"

    print(f"answer is : {answer}")
    

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

        if index == "N":
            print("good bye!")
            break
        elif index == "Y":
            break
        else:
            print("plz type again~")
    if index == "Y":
        continue
    break


        

