#read lower and upper limit from console
#print only the prime numbers between them

lower=int(input("enter lower limit="))
upper=int(input("enter upper limit="))
num=0
for i in range(lower,upper+1):
    if(num%i==0):
        num=1
        break