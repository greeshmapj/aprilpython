class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
pe1=Person("ann",22,"kochi")
pe1.printvalue()

pe2=Person("babu",20,"calicut")
pe2.printvalue()