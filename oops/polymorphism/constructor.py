ept=dept
        self.salary=salary

class Student(Employee,Person):
    def __init__ (self,rollno,college,name,age,place,id,dept,salary):
        Person.__init__(self,name,age,place)
        Employee.__init__(self,id,dept,salary)
        self.rollno=rollno
        self.college=college
    def printstudent(self):
        print(self.name,self.age,self.place,self.id,self.dept,self.salary,self.rollno,self.college)

ob=Student("greeshma",26,"koclass Person:
    def __init__ (self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Employee:
    def __init__ (self,id,dept,salary):
        self.id=id
        self.dtta",123,"python",35000,33,"luminar")
ob.printstudent()