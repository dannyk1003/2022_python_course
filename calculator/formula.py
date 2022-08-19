from commonMethod import commonMethod


class formula(commonMethod):
    def __init__(self, formula):
        # print(formula)
        self.formula = formula
        self.result = []
        self.check_parentheses()

    def check_parentheses(self):
        tmp = ""
        result = []
        for now in self.formula:
            tmp += now
            if (now == '('):
                result.append(tmp[:-1])
                result.append(formula(self.formula[len(tmp):-1]))
                tmp = ""
                break
            # if (now == ')'):
            #     result.append(formula(tmp[:-1]))
            #     tmp = ""
        if (tmp != ""):
            result.append(tmp)
        self.result = result

    def Get_answer(self):
        # print("get answer")
        # print(self.result)
        result_str = ""
        for i in self.result:
            if (isinstance(i, formula)):
                result_str += str(i.Get_answer())
            else:
                result_str += i

        return self.calculator(result_str)

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

    def calculator(self, formula):  # number, operator_count, formula
        '''
        計算區
        '''
        [number, op_list] = self.first_priority(formula)
        answer = number[0]
        if op_list == []:
            return answer
        for i in range(0, len(op_list)):
            if op_list[i] == "+":
                answer += number[i+1]
            elif op_list[i] == "-":
                answer -= number[i+1]
        return answer
