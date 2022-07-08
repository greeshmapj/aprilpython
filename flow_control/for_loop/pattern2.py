#1 2 3 4      #if column vise is same use j
#1 2 3 4
#1 2 3 4
#1 2 3 4

for i in range(1,5):      #1            #2         #3        #4
    for j in range(1,5):  #1  2  3  4   #1 2 3 4   #1 2 3 4  #1 2 3 4
        print(j,end=' ')  #1  2  3  4   #1 2 3 4   #1 2 3 4  #1 2 3 4
    print()