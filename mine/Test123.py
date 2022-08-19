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
        #print(i)
        if i not in operator_element: # formula中存在非formula_element元素
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

def number_counter(formula): # formula, operator_count
    '''
    判斷數字有哪些
    '''
    number = []
    op_counter = operator_counter(formula)
    op_counter.insert(0,-1)
    op_counter.append(len(formula))
    #print(op_counter)

    for i in range(1,len(op_counter)):
        k = ""

        for j in range(op_counter[i-1]+1, op_counter[i]):
            k += formula[j]
        if k == "":
            k_number = None
        else:
            k_number = round(float(k), 2)
        #k_number = int(k)
        number.append(k_number)

    #print(number)
    op_counter.pop(-1)
    op_counter.pop(0)
    return number

formula = "1+2*3+(4+5)+(6/7*(8+9))"
#formula = "1+2*3+9+14.571428571428571"
#formula = "(4+5)"
print("formula=",formula)
print(operator_counter(formula))
print(operator_list(formula))
print(number_counter(formula))



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


def calculator(formula): #number, operator_count, formula
    '''
    計算區
    '''
    number = number_counter(formula)
    op_list = operator_list(formula)
    #op_counter = operator_counter(formula)
    # while True:
    #     #尋找第一個")"，找到後找錢一個"("，把(~)定唯一formula丟入calculator，return answer後取代(~)
    #     formula_left = 
    #     in_side = 
    #     formula_right = 

    [number, op_list] = first_priority(formula)
    #op_list = first_priority(op_counter, op_list, formula)[1]
    #op_list = operator_list(op_counter, formula)
    answer = number[0]
    if op_list == []:
        return answer
  
    #print(operator_list)
    for i in range(0, len(op_list)):
        if op_list[i] == "+":
            answer += number[i+1]
        elif op_list[i] == "-":
            answer -= number[i+1]
        
    return answer


def first_priority(formula): # ["3", "6"], ["+","*"], "123+45*6"
    '''
    先乘除後加減
    '''
    op_list = operator_list(formula)
    #op_counter = operator_counter(formula)
    number = number_counter(formula) # [123,45,6]
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


def is_parentheses_exists(formula):
    for i in list(formula):
        if i in ["(", ")"]:
            return True
    return False        

print(parentheses_inside(formula))
print(calculator(parentheses_inside(formula)))