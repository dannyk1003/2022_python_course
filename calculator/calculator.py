from formula import formula
from commonMethod import commonMethod


class calculator(commonMethod):
    def __init__(self, formula=""):
        self.formula = formula

    def Formula_enter(self):
        '''
        輸入算式
        '''
        formula = input("enter a formula : ")
        formula = self.formula_first_element_is_operator(formula)
        while not self.is_formula(formula):
            print("not a formula, plz type again~")
            formula = input("enter a formula : ")
            formula = self.formula_first_element_is_operator(formula)
        self.formula = formula

        return self

    def Formula_answer(self):
        formulaObj = formula(self.formula)
        return formulaObj.Get_answer()

    def formula_first_element_is_operator(self, formula):
        '''
        如果formula第一個元素是運算元,則在formula前面補0
        '''
        if self.operator_counter(formula) == []:  # formula 沒有運算元
            return "0+" + formula
        elif self.operator_counter(formula)[0] == 0:  # formula 第一個值是運算元,則補0
            return "0" + formula
        else:
            return formula

    def is_formula(self, formula):
        '''
        判斷是否為算式
        '''
        formula_element = ["1", "2", "3", "4", "5", "6",
                           "7", "8", "9", "0", "+", "-", "*", "/", "(", ")"]
        for i in list(formula):
            if i not in formula_element:  # formula中存在非formula_element元素
                return False
        if not self.parentheses_count(formula):  # 左右括號數量是否相同
            return False
        if not self.is_operator_double(formula):  # formula 有相鄰運算元
            return False
        return True

    def parentheses_count(self, formula):
        '''
        計算左右括弧數量是否一致
        '''
        op_list = self.operator_list(formula)
        left_count = op_list.count("(")
        right_count = op_list.count(")")
        if left_count == right_count:
            return True
        else:
            return False

    def is_operator_double(self, formula):  # [3,6]
        '''
        判斷是否有連續的運算元
        '''
        op_counter = self.operator_counter(formula)
        op_list = self.operator_list(formula)
        for i in range(len(op_counter)-1):
            if op_counter[i+1] - op_counter[i] == 1:  # 運算原相鄰
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

    def is_parentheses_exists(self, formula):
        for i in list(formula):
            if i in ["(", ")"]:
                return True
        return False

    def first_priority(self, formula):  # ["3", "6"], ["+","*"], "123+45*6"
        '''
        先乘除後加減
        '''
        op_list = self.operator_list(formula)
        number = self.number_counter(formula)  # [123,45,6]
        first_priority_operator_list = ["*", "/"]
        new_number = []
        new_number.append(number[0])
        new_op_list = []
        for i, j in enumerate(op_list):  # [(0,"+"), (1,"*")]
            if j not in first_priority_operator_list:
                new_number.append(number[i+1])  # 將number存入new_number
                new_op_list.append(op_list[i])
            else:  # 如果有"*" or "/"
                if op_list[i] == "*":
                    new_number[-1] = new_number[-1] * number[i+1]
                elif op_list[i] == "/":
                    new_number[-1] = new_number[-1] / number[i+1]
        return [new_number, new_op_list]

    def number_counter(self, formula):  # formula, operator_count
        '''
        判斷數字有哪些
        '''
        number = []
        op_counter = self.operator_counter(formula)
        op_counter.insert(0, -1)
        op_counter.append(len(formula))
        for i in range(1, len(op_counter)):
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
