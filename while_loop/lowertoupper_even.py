#read lower and upper number and print the even numbers inbetween

low=int(input("enter any number="))
up=int(input("enter any number="))

i=low
while(i<=up):
    if(i%2==0):
       print(i)
    i+=1