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


def formula_first_element_is_operator(formula):
    '''
    如果formula第一個元素是運算元,則在formula前面補0
    '''
    if operator_counter(formula) == []: # formula 沒有運算元
        return "0+" + formula
    elif operator_counter(formula)[0] == 0: # formula 第一個值是運算元,則補0
        return "0" + formula
    else:
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


def is_operator(formula_element):
    '''
    判斷是否為運算元
    '''
    operator_element = ["+", "-", "*", "/", "(", ")"]
    for i in list(formula_element):
        if i not in operator_element: # formula中存在非formula_element元素
            return False
    return True


def is_formula(formula):
    '''
    判斷是否為算式
    '''
    formula_element = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "(", ")"]
    for i in list(formula):
        if i not in formula_element: # formula中存在非formula_element元素
            return False
    if not parentheses_count(formula): # 左右括號數量是否相同
        return False
    if not is_operator_double(formula): # formula 有相鄰運算元
        return False
    return True


def is_operator_double(formula): #[3,6]
    '''
    判斷是否有連續的運算元
    '''
    op_counter = operator_counter(formula)
    op_list = operator_list(formula)
    for i in range(len(op_counter)-1):
        if op_counter[i+1] - op_counter[i] == 1: # 運算原相鄰
            if op_list[i] in ["+", "-", "*", "/"]:
                if op_list[i+1] != "(":
                    return False
            if op_list[i] == "(":
                if op_list[i+1] in ["+", "-", "*", "/"]:
                    return False
            if op_list[i] == ")":
                if op_list[i+1] == "(":
                    return False
    return True


def operator_list(formula): # x = operator_count [3, 6], y = formula
    '''
    運算原有哪些(加順序)
    '''
    op_counter = operator_counter(formula)
    op_list = []
    formula_list = list(formula)
    for i in op_counter:
        op_list.append(formula_list[i])
    return op_list #["+","+"]


def parentheses_count(formula):
    '''
    計算左右括弧數量是否一致
    '''
    op_list = operator_list(formula)
    left_count = op_list.count("(")
    right_count = op_list.count(")")
    if left_count == right_count:
        return True
    else:
        return False 


def parentheses_inside(formula):  
    while is_parentheses_exists(formula):
        op_list = operator_list(formula)
        op_counter = operator_counter(formula)
        for i, j in enumerate(op_list):
            if j == ")":
                right_op_counter = i # i = 6
                #op_counter[i] # i=6, op_counter[i]=10
                for k in list(range(i, -1, -1)):
                    if op_list[k] == "(":
                        left_op_counter = k # k = 4
                        break
                break
        left_counter = op_counter[left_op_counter] # 6
        right_counter = op_counter[right_op_counter] # 10
        in_formula = ""
        for i, j in enumerate(list(formula)):
            if i > left_counter and i < right_counter:
                in_formula = in_formula + j
        in_number = calculator(in_formula)
        left_formula = ""
        right_formula = ""
        for i, j in enumerate(list(formula)):
            if i < left_counter:
                left_formula = left_formula + j
        for i, j in enumerate(list(formula)):
            if i > right_counter:
                right_formula = right_formula + j
        new_formula = left_formula + str(in_number) + right_formula
        formula = new_formula
    
    return formula


def is_parentheses_exists(formula):
    for i in list(formula):
        if i in ["(", ")"]:
            return True
    return False 


def calculator(formula): #number, operator_count, formula
    '''
    計算區
    '''
    [number, op_list] = first_priority(formula)
    answer = number[0]
    if op_list == []:
        return answer
    for i in range(0, len(op_list)):
        if op_list[i] == "+":
            answer += number[i+1]
        elif op_list[i] == "-":
            answer -= number[i+1]  
    return answer


def number_counter(formula): # formula, operator_count
    '''
    判斷數字有哪些
    '''
    number = []
    op_counter = operator_counter(formula)
    op_counter.insert(0,-1)
    op_counter.append(len(formula))
    for i in range(1,len(op_counter)):
        k = ""
        for j in range(op_counter[i-1]+1, op_counter[i]):
            k += formula[j]
        if k == "":
            k_number = None
        else:
            k_number = round(float(k), 2)
        number.append(k_number)
    op_counter.pop(-1)
    op_counter.pop(0)
    return number


def first_priority(formula): # ["3", "6"], ["+","*"], "123+45*6"
    '''
    先乘除後加減
    '''
    op_list = operator_list(formula)
    number = number_counter(formula) # [123,45,6]
    first_priority_operator_list = ["*", "/"]
    new_number = []
    new_number.append(number[0])
    new_op_list = []
    for i, j in enumerate(op_list): # [(0,"+"), (1,"*")]
        if j not in first_priority_operator_list:
            new_number.append(number[i+1]) # 將number存入new_number
            new_op_list.append(op_list[i])
        else: # 如果有"*" or "/"
            if op_list[i] == "*":
                new_number[-1] = new_number[-1] * number[i+1]
            elif op_list[i] == "/":
                new_number[-1] = new_number[-1] / number[i+1]
    return [new_number, new_op_list]


def try_again():
    '''
    是否要再來一次
    '''
    while True:
        index = input("continue?(Y/N):")
        if index.upper() == "N":
            print("good bye!")
            break
        elif index.upper() == "Y":
            print("U can enter formula again~")
            main()
            break
        else:
            print("plz type again~")


def main():
    '''
    counter3.2 main function
    '''
    formula = formula_enter() 
    final_formula = parentheses_inside(formula) 
    answer = calculator(final_formula)
    print(f"{formula} = {answer}") 
    try_again() 


main()