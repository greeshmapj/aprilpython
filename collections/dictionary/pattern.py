#PATTERN

#pattern='ABCDBCDEF'

#find the first recurssive character
#dic={}
#for i in pattern:
#    if i not in dic:
#        dic[i]=1
#    else:
#        print("first recurssive chracter is ",i)
#        break

lst=[1,3,4,5,4,3,2,7,8,9,3,4,2,1,9,10,11,12,15,13,12,11,10,9,5]
#lst=[1,3,5,6,8,9,6,4,3,2,5,8,9]
#creat a new list from this with characters 1,5,2,9,3,4,1,15

#LOGIC IS INCREASE OR DECREASE

for i in range(0,len(lst)):
    if(lst[i-1]<lst[i]>lst[i+1])or(lst[i-1]>lst[i]<lst[i+1]):
        print(lst[i])

