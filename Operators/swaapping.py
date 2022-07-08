num1=10
num2=20   #swapping

print("number1=",num1)
print("number2=",num2)    #before swapping

temp=num1  #temp=10
num1=num2  #num1=20
num2=temp  #num2=10

print(num1)
print(num2)   #after swapping

num1=30
num2=40
print(num1)
print(num2)   #before swapping

num1=num1+num2     #30+40=70
num2=num1-num2     #70-40=-30
num1=num1-num2  #after swapping  #70-30=40
print(num1)
print(num2)




#num1=10
#num=20

num1,num2=10,20   #same as above written


num1,age,name,location=10,26,'greeshma','kakkanad'
print(location)



num1,num2=50,60
num1,num2=num2,num1
print(num1)
print(num2)  #single line swapping
