def is_number():
    '''
    輸入數字並判斷是否為數字
    '''
    checker = 0
    while checker != 1:
        x = input("enter number:")
        number_len = 0
        for i in x:
            if i not in str(list(range(10))):
                print("not a number!")
                break
            else:
                number_len += 1
        if number_len == len(x):
            checker = 1  
    return int(x)


def main():

    x = is_number()

    y = is_operator()
        
    z = is_number()

    answer = count_area(x, y, z)

    print(f"{x} {y} {z} = {answer}")

    try_again()

    
def is_operator():
    '''
    輸入運算元並判斷是否為運算元
    '''
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
    return y


def try_again():
    '''
    是否要再來一次
    '''
    while True:
        index = input("countinue?(Y/N):")
        #print(index)
        #print(index == "N")

        if index.upper() == "N":
            print("good bye!")
            break
        elif index.upper() == "Y":
            print("U can enter number again~")
            main()
        else:
            print("plz type again~")


def count_area(x,y,z):
    '''
    計算區
    '''
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

    return answer

main()
