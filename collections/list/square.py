#print the square o these elements


lst=[10,20,30,40,50,60,70,80]
#for i in lst:

 #   print(i**2)

#print the corresponding power
#10**1
#20**2
#30**3....

count=1
for i in lst:
    res=i**count
    count+=1
    print(res)
