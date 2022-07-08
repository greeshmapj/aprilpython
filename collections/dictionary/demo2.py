#name,age,pro,salary
#update name to fname
#print value of pro alone
#check if a key company is present in the dic
#include company='luminar'
#add 5000 to salary
#print key value pairs


dic={"name":'greeshma',"age":26,"pro":'engineer',"salary":35000}

print(dic["pro"])
print("company" in dic)

dic["company"]='luminar'
print(dic)

dic["salary"]=40000
print(dic)

for i in dic:
    print(i,dic[i])


