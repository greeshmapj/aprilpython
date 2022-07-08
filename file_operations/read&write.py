#read data file and write it to a diferent file

f=open("data","r")

f1=open("data1","w")
for i in f:
    f1.write(i)
