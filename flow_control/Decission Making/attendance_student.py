
number_of_classes_held=100
classes_attended=int(input("enter no. of classes attended"))
attendance=((classes_attended/100)*100)
print("attendance is ",attendance,"%")
if(attendance>=75):
    print("allowed to sit for exam")
else:
    print("not eligible")