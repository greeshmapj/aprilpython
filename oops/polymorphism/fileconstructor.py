class Student:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printval(self):
        print(self.name,self.age,self.place)
f=open("student.py","r")
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    place=data[2]
    ob=Student(name,age,place)
    ob.printval()