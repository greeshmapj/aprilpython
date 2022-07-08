#factorial
#5 :5*4*3*2*1

#calculate the factorial of a number using functions with all the 3 methods


#method1
#def fact():
#    num1=int(input('enter any number='))
#    fac=1
#    for i in range(1,num1+1):
#       fac=fac*i
#    print(fac)

#fact()


#method2
#def fact(num1):
#   fac=1
#   for i in range(1,num1+1):
#       fac=fac*i
#   print(fac)

#fact(4)



#method3
#def fact(num1):
#    fac=1
#    for i in range(1,num1+1):
#      fac=fac*i
#    return fac

#data=fact(5)
#print(data)



#find cube of a number

#method1
#def cube():
#    num=int(input('enter any number='))
#    cu=num*num*num
#    print(cu)
#cube()


#method2
#def cube(num):
#  cu=num*num*num
#   print(cu)
#cube(3)


#method3
#def cube(num):
#    cu=num*num*num
#    return cu
#data=cube(4)
#print(data)




#create a calculator
#1.addition
#2.subtraction
#3.multiplication
#4.division

#enter ur choice
#num1
#num2

#***************************8
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2


def div(num1,num2):
    return num1/num2

print("1.addition\n")
print("2.subtraction\n")
print("3.multiplication\n")
print("4.division\n")

choice=int(input("enter your choice="))
num1=int(input('enter number1='))
num2=int(input('enter number2='))

if(choice==1):
    print(num1,"+",num2,"=",add(num1,num2))
elif(choice==2):
    print(num1,"-",num2,"=",sub(num1,num2))
elif(choice==3):
    print(num1,"*",num2,"=",mul(num1,num2))
elif(choice==4):
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("invalid")









