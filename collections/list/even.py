#make a empty list and to it add 1 to 75 then from it create a list of even number and odd no.
#then print the sum of even no. and sum of odd no.

lst=[]
for i in range(1,76):
   lst.append(i)
print(lst)
print(sum(lst))

lst1=[]
lst2=[]
for i in lst:
    if (i%2==0):
        lst1.append(i)
    else:
        lst2.append(i)

print(lst1)
print(sum(lst1))
print(lst2)
print(sum(lst2))
