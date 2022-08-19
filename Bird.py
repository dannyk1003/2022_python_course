class bird:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(self.__str__(),'walking...')
    def mew(self):
        print(self.__str__(),'mew')
    def __str__(self):
        return self.name
