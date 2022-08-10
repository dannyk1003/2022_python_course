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
    formula = formula_first_element_is_operator(formula)
    while not is_formula(formula):
        print("not a formula, plz type again~")
        formula = input("enter a formula : ")
        formula = formula_first_element_is_operator(formula)
    return formula


def operator_counter(formula):
    '''
    判斷哪幾個是運算元;
    x = formula;
    return = list[ ]
    '''
    op_counter = []
    for i, formula_element in enumerate(list(formula)):
        #enumerate 將內容編號 [(0, "A"), (1, "B"), (2, "C")...]
        if is_operator(formula_element):
            op_counter.append(i)
    return op_counter


def is_operator_double(op_counter): #[3,6]
    '''
    判斷是否有連續的運算元
    '''
    for i in range(len(op_counter)-1):
        if op_counter[i+1] - op_counter[i] == 1:
            return False
    return True


def is_operator(formula_element):
    '''
    判斷是否為運算元
    '''
    if formula_element == "+":
        return True
    elif formula_element == "-":
        return True
    elif formula_element == "*":
        return True
    elif formula_element == "/":
        return True
    #elif formula_element == "=":
    #    return True
    else:
        return False


def number_counter(formula, operator_count): # formula, operator_count
    '''
    判斷數字有哪些
    '''
    number = []
    operator_count.insert(0,-1)
    operator_count.append(len(formula))
    #print(operator_count)

    for i in range(1,len(operator_count)):
        k = ""

        for j in range(operator_count[i-1]+1, operator_count[i]):
            k += formula[j]
        
        k_number = int(k)
        number.append(k_number)

    #print(number)
    operator_count.pop(-1)
    operator_count.pop(0)
    return number


def operator_list(operator_count, formula): # x = operator_count [3, 6], y = formula
    '''
    運算原有哪些(加順序)
    '''
    op_list = []
    formula_list = list(formula)
    for i in operator_count:
        op_list.append(formula_list[i])
    
    return op_list #["+","+"]


def calculater(number, operator_count, formula): #number, operator_count, formula
    '''
    計算區
    '''
    op_list = operator_list(operator_count, formula)

    [number, op_list] = first_priority(operator_count, op_list, formula)
    #op_list = first_priority(operator_count, op_list, formula)[1]
    #op_list = operator_list(operator_count, formula)
    answer = number[0]
  
    #print(operator_list)
    for i in range(0, len(op_list)):
        if op_list[i] == "+":
            answer += number[i+1]
        elif op_list[i] == "-":
            answer -= number[i+1]
        
    return answer


def is_formula(formula):
    '''
    判斷是否為算式
    '''
    formula_element = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/"]
    for i in list(formula):
        #print(i)
        if i not in formula_element: # formula中存在非formula_element元素
            #print(formula_element)
            return False
    if not is_operator_double(operator_counter(formula)): # formula 有相鄰運算元
        return False

    return True


def formula_first_element_is_operator(formula):
    '''
    如果formula第一個元素是運算元,則在formula前面補0
    '''
    if operator_counter(formula)[0] == 0: # formula 第一個值是運算元,則補0
        return "0" + formula
    else:
        return formula
        

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
            break
        else:
            print("plz type again~")


def first_priority(operator_count, op_list, formula): # ["3", "6"], ["+","*"], "123+45*6"
    '''
    先乘除後加減
    '''
    number = number_counter(formula, operator_count) # [123,45,6]
    first_priority_operator_list = ["*", "/"]
    new_number = []
    new_number.append(number[0])
    new_op_list = []
    
    print(number,op_list)
    for i, j in enumerate(op_list): # [(0,"+"), (1,"*")]
        if j not in first_priority_operator_list:
            new_number.append(number[i+1]) # 將number存入new_number
            new_op_list.append(op_list[i])
            print(new_number)
        else: # 如果有"*" or "/"
            #n = new_number[-1]
            #new_number.pop()
            #new_op_list.pop()
            if op_list[i] == "*":
                new_number[-1] = new_number[-1] * number[i+1]
            elif op_list[i] == "/":
                new_number[-1] = new_number[-1] / number[i+1]
            
        print([new_number, new_op_list])    
            #把乘除的移到最前面
            #把乘除先算完
    return [new_number, new_op_list]




def main():
    '''
    counter2.0 main function
    '''
    formula = formula_enter() 
    #formula = ["123+45+6"]
    operator_count = operator_counter(formula) 
    #operator_count = [3,6]
    number = number_counter(formula, operator_count) 
    #number = [123,45,6]
    answer = calculater(number, operator_count, formula) 
    #answer = 174
    print(f"{formula} = {answer}") 
    #print : "123+45+6 = 174"
    try_again() 
    #print : "countinue?(Y/N):"


main()

'''
乘和除想法:
1. 先乘除後加減
    1.1 先把乘和除的位置找出
    1.2 乘和除的先後先算，算完後合成一個
    1.3 再列出計算加減
'''