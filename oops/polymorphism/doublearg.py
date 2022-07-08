#dic1={'physics':56,'maths':65,'history':80}
#print(min(dic1,key=dic1.get))

#encapsulation
class Person:
    def __init_(self):
        self.name="arun"
        self._salary=3000
        self.__age=25
    def printval(self):
        print("inside class Person",self.name,self._salary,self.__age)

class Employee(Person):
    def __init__(self):
        self.id=id
        self.desig=desig
        self.salary=salary
        print("inside class Employee",self.id,self.desig,self.salary,self.name,self.__age)

ob=Employee()
ob.printa("greeshma",26)
ob.printc(123,"engineer",50000)
ob.printa()