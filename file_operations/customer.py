f=open("C:/Users/SuperUser/Downloads/Customer","r")
#for i in f:
#    print(i)
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    prof=data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
print(dic)

#or age>50,fname,lname,prof





