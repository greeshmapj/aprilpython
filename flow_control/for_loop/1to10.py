#print 1 to 10 using for loop


for i in range(1,11):
    print(i)



#if need to print 3,6,9,12....

for i in range(3,19,3):     #lower limit,upper limi, increment/decremennt
    print(i)





for i in range(10):  #0 to 9
    print(i)


for i in range (20,10,-2):
    print(i)

#print 20 to 1
for i in range(20,0,-1):
    print(i)




#print 1 from desired number

num=int(input("enter any number"))
for i in range(1,num):
    print(i)


#print lower to upper number

lower=int(input("enter lower limit="))
upper=int(input("enter upper limit="))
for i in range(lower,upper+1):
    print(i)


#print even numbers between the range
lower=int(input("enter lower limit="))
upper=int(input("enter upper limit="))
for i in range(lower,upper+1):
    if(i%2==0):
         print(i)




#sum of n numbers
num=int(input("enter any number"))
sum=0
for i in range(1,num+1):
    sum+=i
print(sum)


#calculate the sum of odd and even numbers
lower=int(input("enter lower limit"))
upper=int(input("enter upper limit="))
even=0
odd=0
for i in range(lower,upper+1):
  if(i%2==0):
      even+=i
  else:
      odd+=i
print(even)
print(odd)


