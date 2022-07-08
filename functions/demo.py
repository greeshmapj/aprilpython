#functions
#for reusability
# eg of inbulit functions:print(),input(),type


#num1=int(input('enter number1'))
#num2=int(input('enter number2'))
#sum=num1+num2
#print(sum)

#if we have to add 2 more numbers then we need not repeat the entire code we can just call the fuction



#how to create a function
#there are 3 methods

#1.function without argument and no return value
#2.function with argument and no return value
#3.functions with argument and return value

#[argument=variables]

#basic syntax is
#***********************************
#def fnname (arguments):
#    fn definition      #code of the task to be performed

#fnname()
#***********************************



#method1
#function without argument and no return type

#def add():
#  num1=int(input('enter number1='))
#   num2=int(input('enter number2='))
#   sum=num1+num2
#   print(sum)
#add()

#add()





#for dividing to numbers write the code
#def div():
#   num1=int(input('enter num1='))
#   num2=int(input('enter num2='))
#   division=num1/num2
#   print(division)
#div()



#method2
#function with arguments and no return type
#def add(num1,num2):
#   sum=num1+num2
#   print(sum)

#add(30,50)


#find product of 2 no.s using method2

#def mul(num1,num2):
#   product=num1*num2
#   print(product)
#mul(30,2)



#method3
#function with argument and return type
#def add(num1,num2):
#   sum=num1+num2
#   return sum               #return means it does not use the output,gives to someone else

#data=add(25,30)
#data1=add(40,50)

#print(data)
#print(data1)


#write a code to subtract 2 no.s using method3

def minus(num1,num2):
    diff=num1-num2
    return diff

data=minus(50,10)
print(data)