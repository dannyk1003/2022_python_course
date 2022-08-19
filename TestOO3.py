class C:
    def __init__(self):
        print('C constructor is called') # 呼叫自己(C)

class D(C):
    pass #自己沒有 -> 叫父類別(C)

class E(C):
    def __init__(self):
        print('E constructor is called') # 呼叫自己(E)

class F(E):
    def __init__(self):
        #super().__init__() # 呼叫父類別(E)
        print('F constructor is called') # 呼叫自己(F)
        super().__init__() # 呼叫父類別(E)

c = C()
d = D() # 未定義建構子 -> 繼承父類別的建構子
e = E() # 有定義建構子 -> 用自己的建構子
f = F() # 利用super().__init__() -> 呼叫父類別
