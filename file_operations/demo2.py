#read the numbers file and update to a  empty list nf find its sum
#make 2 lists of odd and even numbers and find there sum

f=open("numbers","r")
lst=[]
evn_lst=[]
odd_lst=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)

for i in lst:
    if(i%2==0):
        evn_lst.append(i)
    else:
        odd_lst.append(i)

print(evn_lst)
print(odd_lst)
print(sum(evn_lst))
print(sum(odd_lst))



