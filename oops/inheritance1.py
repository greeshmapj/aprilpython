class Person:
    def printa(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print("inside class Person",self.name,self.age,self.place)

class Student(Person):
    def printb(self,roll,dept):
        self.roll=roll
        self.dept=dept
        print("inside class Student",self.roll,self.dept,self.name,self.age,self.place)

b=Student()
b.printa("greeshma",26,"kottayam")
b.printb(33,"python")