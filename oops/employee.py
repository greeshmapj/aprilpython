class Person:
    def printa(self,name,age):
        self.name=name
        self.age=age
        print("inside class Person",self.name,self.age)

class Parent:
    def printb(self,place,phone):
        self.place=place
        self.phone=phone
        print("inside class Parent",self.place,self.phone)

class Employee(Person,Parent):
    def printc(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
        print("inside class Employee",self.id,self.desig,self.salary,self.name,self.age,self.place,self.phone)

ob=Employee()
ob.printa("greeshma",26)
ob.printb("kottayam",8921129049)
ob.printc(123,"engineer",50000)