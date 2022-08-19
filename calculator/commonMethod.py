class commonMethod:
    def operator_list(self, formula):  # x = operator_count [3, 6], y = formula
        '''
        運算原有哪些(加順序)
        '''
        op_counter = self.operator_counter(formula)
        op_list = []
        formula_list = list(formula)
        for i in op_counter:
            op_list.append(formula_list[i])
        return op_list  # ["+","+"]

    def operator_counter(self, formula):
        '''
        判斷哪幾個是運算元;
        x = formula;
        return = list[ ]
        '''
        op_counter = []
        for i, formula_element in enumerate(list(formula)):
            # enumerate 將內容編號 [(0, "A"), (1, "B"), (2, "C")...]
            if self.is_operator(formula_element):
                op_counter.append(i)
        return op_counter

    def is_operator(self, formula_element):
        '''
        判斷是否為運算元
        '''
        operator_element = ["+", "-", "*", "/", "(", ")"]
        for i in list(formula_element):
            if i not in operator_element:  # formula中存在非formula_element元素
                return False
        return True
