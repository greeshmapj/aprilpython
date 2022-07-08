#read 3 no.s rom console and find the second largest number

num1=int(input("enter number1="))      #100
num2=int(input("enter number2="))       #60
num3=int(input("enter number3="))       #80    #nested if

if(num1>num2)&(num1>num3):      #100>80 & 100>60
    if(num2>num3):
        print("n2 is second largest")
    else:
        print("n3 is second largest")
elif(num2>num3)&(num2>num1):
    if(num3>num1):
        print("n3 is second largest")
    else:
        print("n1 is second largest")
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("n1 is second largest")
    else:
         print("n2 is second largest")
