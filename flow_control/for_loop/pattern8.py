#1               #different values hence  need to be j need to be printed also j is showing decrement
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1

for i in range(1,6):         #1          #2
    for j in range(i,0,-1):  #(1,0)j=1   #(2,0)j=2,1
        print(j,end=' ')     #1          #2 1
    print()
    

