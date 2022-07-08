class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")
    def __str__(self):
        return self.course_name

    @property           #using this we can access the method as a property
    def get_name(self):
        print(self.course_name)
        return self.course_name

class Batch():
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self):
        return self.batch_code

class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.batch=kwargs.get("batch")
        self.email=kwargs.get("email")
    def __str__(self):
        return self.student_name

django=Course()
django.add_course(course_name="django",status=True)
#bd=Course()
#bd.add_course(course_name="bigdata",status=True)

djb1=Batch()
djb1.add_batch(course=django,batch_code="djmay2k22b1",start_date="12-06-2022")

rahul=Student()
rahul.add_student(student_name="rahul",batch_code=djb1,email="rahul@gmail.com")
akhil=Student()
akhil.add_student(student_name="akhil",batch_code=djb1,email="akhil@gmail.com")
vishnu=Student()
vishnu.add_student(student_name="vishnu",batch_code=djb1,email="vishnu@gmail.com")

mearnstack=Course()
mearnstack.add_course(course_name="mearnstack",status=True)

msb1=Batch()
msb1.add_batch(course=mearnstack,batch_code="msaprb1",start_date="15-06-2022")

veena=Student()
veena.add_student(student_name="veena",batch_code=msb1,email="veena@gmail.com")
maria=Student()
maria.add_student(student_name="maria",batch_code=msb1,email="maria@gmail.com")

students=[]
students.append(veena)
students.append(maria)
students.append(akhil)
students.append(vishnu)
students.append(rahul)

#prints students from ms only
for stud in students:
   if stud.batch.course=="mearnstack":
        print(stud)
#ms_stud=[stud.student_name for stud in students if stud.batch.course.course_name=="mearnstack"]
#print(ms_stud)











