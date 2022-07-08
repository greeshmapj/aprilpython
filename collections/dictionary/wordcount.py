#WORDCOUNT PROGRAM

line='cat rat bus cat car car rat bus car car bus cat'
data=line.split(' ')
print(data)

#['cat', 'rat', 'bus', 'cat', 'car', 'car', 'rat', 'bus', 'car', 'car', 'bus', 'cat']
dic={}

#key  value
#cat,2
#rat,1
#bus,1
#car,2

for i in data:
   if i not in dic:
        dic[i]=1
   else:
       dic[i]+=1

print(dic)


