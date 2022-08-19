class C:
    def __init__(self, name):
        self.name = name
        print('C constructor is called : ' , self.name) # 呼叫自己(C)

class D(C):
    def __init__(self, name):
        self.name = name
        super().__init__(self.name) # 呼叫父類別的__init__，帶入自己的name
        print('D constructor is called : ' , self.name) # 呼叫自己(C)


c = C('Alan')
d = D('Bob')