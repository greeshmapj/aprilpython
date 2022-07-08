#read a number and print its multiplication table

num=int(input("enter any number="))

i=1
while(i<=10):
    res=num*i
    print(num,"*",i,"=",res)
    i+=1