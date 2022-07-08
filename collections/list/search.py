#read a element from the console, i it is found in the list print element found
#else element not found
#LINEAR SEARCH

lst=[10,15,6,3,22,66,70,89]
number=int(input('enter any number='))
flg=0
for i in lst:
    if(number==i):
        flg=1
        break
if(flg>0):
    print("element found")
else:
    print("element not found")