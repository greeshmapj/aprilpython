#read lower limit and upper limit and print the sum of odd & even no.s inbetween

low=int(input("enter any lower limit number="))
up=int(input("enter any upper limit number="))

i=low
sum1=0
sum2=0
while(i<=up):
    if(i%2==0):
        sum1+=i
    else:
        sum2+=i
    i+=1
print(sum1)
print(sum2)

