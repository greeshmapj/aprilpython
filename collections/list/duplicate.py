#make a list from the given list avoiding the duplicate elements


#for i 'luminar'
#if i in lst:               #if i is present in list
#if i not in lst:           #if i is not present in the list

lst=[10,10,20,20,30,30,40,50,50,60,70,80,80]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)