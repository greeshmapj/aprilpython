class Employee:
    def setvalue(self,name,id,desig,salary,company):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary
        self.company=company
    def printvalue(self):
        print(self.name)
        print(self.id)
        print(self.desig)
        print(self.salary)
        print(self.company)
em1=Employee()
em1.setvalue("ann",44,"engineer",400000,"kits")
em1.printvalue()

em2=Employee()
em2.setvalue("mary",63,"zoology","saint gits")
em2.printvalue()

em3=Employee()
em3.setvalue("oseph",35,"maths","alphonsa")
em3.printvalue()