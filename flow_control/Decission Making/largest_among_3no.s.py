
num1=int(input("enter number1"))      #100(1st)   #80  #60
num2=int(input("enter number2"))      #
num3=int(input("enter number3"))

if(num1>num2):
    if(num1>num3):
        print("num1 is greater")
    else:
        print("num3 is greater")
else:
    print("num2 is greater")


    #OR

if(num1>num2)&(num1>num3):
    print("num1 is greater",num1)
elif(num2>num3)&(num2>num1):
    print("num2 is largest",num2)
else:
    print("num3 is largest")

