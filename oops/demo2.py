class Student:
    def setvalue(self,name,rollno,department,college_name):
        self.name=name
        self.rollno=rollno
        self.department=department
        self.college_name=college_name
    def printvalue(self):
        print(self.name)
        print(self.rollno)
        print(self.department)
        print(self.coolege_name)
st1=Student()
st1.setvalue("ann",44,"biology","kvrb")
st1.printvalue()

st2=Student()
st2.setvalue("mary",63,"zoology","saint gits")
st2.printvalue()

st3=Student()
st3.setvalue("oseph",35,"maths","alphonsa")
st3.printvalue()




