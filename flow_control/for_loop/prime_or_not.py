#check whether the  number is prime or not        #***important for interview

#2 3 5 7 9

#9  (2,8)
#13  (2,12)

num=int(input("enter any number="))
flg=0
for i in range(2,num):
    if(num%i==0):    #9%2=1   #9%3==0
        flg=1
        break

if(flg>0):
    print("not prime")
else:
    print("prime")
