class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def test1(self):
        print('call test1')
    def test2(self):
        print('call test2')
    def test3(self):
        print(f'a+b+c={self.a}+{self.b}+{self.c}')


a = A(1,2,3)
a.test1()
a.test2()
a.test3()

'''
類別(class):
    建構子(constructor) -> __init__
    屬性(field) -> a, b, c
    方法(method) -> function

物件導向:
    封裝(class, function)
    繼承(super, class(father))
    多形(type)

'''
