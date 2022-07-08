class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printval(self):
        print(self.name,self.age,self.place)

class Student(Person):
    def __init__(self,rollno,dept,college,name,age,place):
        super().__init__(name,age,place)
        self.rollno=rollno
        self.dept=dept
        self.college=college
    def printstu(self):
        print(self.rollno,self.dept,self.college)
ob=Student("babu",26,"kotta",333,"biology","kits")
ob.printstu()
ob.printval()