'''
1. 輸入算式
1.1 判斷第幾個是運算元
    1.1.1 if [2,5] 是運算元
    1.1.2 then [0:2,3:5] 是數字
    1.1.3 "=" 只能是最後一個運算元
1.2 判斷幾個數字(長度)
1.3 判斷幾個運算元

2. 計算結果
'''
def formula_enter():
    '''
    輸入算式
    '''
    formula = input("enter a formula : ")
    while not is_formula(formula):
        print("not a formula, plz type again~")
        formula = input("enter a formula : ")
    return formula


def main():
    formula = formula_enter()
    operator_count = operator_counter(formula)
    number = number_counter(formula, operator_count)
    answer = calculater(number, operator_count, formula)
    print(f"{formula} = {answer}")
    try_again()

def operator_counter(x):
    '''
    判斷第幾個是運算元
    '''
    operator_counter = []
    j = -1
    for i in list(x):
        j += 1
        if is_operator(i):
            operator_counter.append(j)

    return operator_counter


def is_operator(x):
    '''
    判斷是否為運算元
    '''
    if x == "+":
        return True
    elif x == "-":
        return True
    elif x == "*":
        return True
    elif x == "/":
        return True
    elif x == "=":
        return True
    else:
        return False


def number_counter(x, y):
    '''
    判斷數字有哪些
    '''
    number = []
    y.insert(0,-1)
    y.append(len(x))
    #print(y)

    for i in range(1,len(y)):
        k = ""

        for j in range(y[i-1]+1, y[i]):
            k += x[j]
        
        k_number = int(k)
        number.append(k_number)

    #print(number)
    y.pop(-1)
    y.pop(0)
    return number


def calculater(x, y, z):
    '''
    計算區
    '''
    formula_list = list(z)
    operator_list = []
    answer = x[0]
    for i in y:
        operator_list.append(formula_list[i])
    
    #print(operator_list)
    for i in range(0, len(operator_list)):
        if operator_list[i] == "+":
            answer += x[i+1]
        elif operator_list[i] == "-":
            answer -= x[i+1]
        
    return answer


def is_formula(x):
    '''
    判斷是否為算式
    '''
    formula_len = 0
    formula_element = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-"]
    for i in list(x):
        #print(i)
        if i not in formula_element:
            #print(formula_element)
            return False
            break
        else:
            formula_len += 1
    if formula_len == len(x):
        return True


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
            print("U can enter formula again~")
            main()
        else:
            print("plz type again~")


main()
