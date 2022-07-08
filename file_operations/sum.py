#read sum file and update it to a list and find the sum of the list

f=open("numbers","r")

lst=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
print(sum(lst))

