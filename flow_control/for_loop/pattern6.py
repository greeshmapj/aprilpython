#5 5 5 5 5    #since row vise same we have to print i
#4 4 4 4
#3 3 3
#2 2
#1

for i in range(5,0,-1):   #5                   #4
 for j in range(0,i):     #(0,5)j=0 1 2 3 4    #(0,4)j=0,1,2,3
     print(i,end=' ')     #5 5 5 5 5           #4 4 4 4
 print()