lst=[4,5,10,12,20]

#we have to create a new list from this with elements [47,46,41,39,31].find logic?
#sum=4+5+10+12+20=51
#51-4=47
#51-5=46
#51-10=41
#51-12=39
#51-20=31

#logic
#lst=[4,5,10,12,20]
#total=(sum(lst))
#lst1=[]
#for i in lst:
#    res=total-i
#    lst1.append(res)

#print(lst1)


#lst=[3,5,15,20,25]
#make a new list with [65,63,53,48,43]


#QUESTION3.
lst=[4,3,2,1]
#for an element that we read from the console print its pair
#for eg: if we read 6 we have to print(2,4) or(3,3

number=int(input("enter an element="))
lst.sort()
low=0
upp=len(lst)-1

while(low<=upp):
    data=lst[low]+lst[upp]

    if(data==element):
        print("pairs are",lst[low],lst[upp])
        break

    elif(data>element):
        upp=upp-1

    else:
        low=low+1

