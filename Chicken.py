from Bird import bird
class chicken(bird):
    def wu(self):
        print(self.__str__(), "Co Co~")
    def __str__(self):
        #return self.name
        #return 'differet~'
        #return 'new ' + super().__str__()
        return '['+super().__str__()+']'

#self 此類別
#super() 父類別