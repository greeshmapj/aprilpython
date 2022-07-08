#read a number from console and print the sum from 1 t0 no.

num=int(input("enter any number="))

i=1
sum=0
while(i<=num):    #1<=6  #2<=6 #3<=6
    sum+=i        #0+1=1  #1+2=3  #3+3=6
    i+=1
print(sum)   #since we need only the final answer print placed outside the loop
