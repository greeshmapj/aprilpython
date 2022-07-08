class Employee:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def printval(self):
        print(self.fname,self.lname,self.age)
f=open("C:/Users/SuperUser/Downloads/Customer","r")
for i in f:
    lst=[]
    data=i.rstrip("\n").split(",")
    fname=data[1]
    lname=data[2]
    age=data[3]
    ob=Employee(fname,lname,age)
    print(ob.fname)
    lst.append((ob.fname,ob.lname,ob.age))
    print(lst)