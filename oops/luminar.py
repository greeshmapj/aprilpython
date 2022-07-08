class Luminar:
    institution="luminar"
    fees=30000
    def setvalue(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age

    def printvalue(self):
        print(self.name)
        print(self.roll)
        print(self.age)
        print(Luminar.institution)
        print(Luminar.fees)


lu1=Luminar()
lu1.setvalue("greeshma",33,26)
lu1.printvalue()

lu2=Luminar()
lu2.setvalue("nasheer",88,10)
lu2.printvalue()

lu3=Luminar()
lu3.setvalue("nisha",51,23)
lu3.printvalue()