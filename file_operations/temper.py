#find the maximum temperature in each district

f=open("C:/Users/SuperUser/Downloads/Temper","r")
dic={}
old_temp=0
dis=data[0]
tem=data[1]
for i in f:
    data=i.rstrip("\n").split(" ")
    if dis not in dic:
        dic[dis]=tem
    else:
        old_temp=dic[dis]
print(dic)