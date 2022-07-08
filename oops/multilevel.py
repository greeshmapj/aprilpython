class Person:
    def seta(self,name,age):
        self.name=name
        self.age=age
        print("inside class A",self.name,self.age)

class Child(Person):
    def setb(self,place,school):
        self.place=place
        self.school=school
        print("inside class B",self.place)

class Student(Child):
    def setc(self,roll,dept,college):
        self.roll=roll
        self.dept=dept
        self.college=college
        print("inside class C",self.dept,self.college)

ob=Student()
ob.seta("greeshma",26)
ob.setb("kottayam","v")
ob.setc(22,"biology","kits")