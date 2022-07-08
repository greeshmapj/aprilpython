#sabir binarysearch

#lst=[7,4,3,1,2]
#steps to follow
#1.sort the list in ascending ordr
#[1,2,3,4,7]

#2.declare 2 variables
#low=0
#upper=len(lst)-1  :4

#3.calculate the mid value
#mid=(low+up)//2    :(0+4)//2=2

#check 3 conditions
#a. search element>lst[mid]   #4>3
  #then low=mid+1

#b. search element<lst[mid].
   #then up=mid-1

#c. searc element==lst[mid]  #element found

lst=[2,3,1,10,15,13,14,12,11,4]
lst.sort()
print(lst)

element=int(input("enter the element="))
low=0
up=len(lst)-1
flag=0
while(low<=up):
    mid=(low+up)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<=lst[mid]):
        up=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("not found")




















