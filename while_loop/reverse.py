#read a num(153) and print its reverse(351)

#153
#153%10:3
#153//10=15

#15%10:5
#15//10=1

#1%10:1


num=int(input("enter any number="))

res=0
while(num!=0):   #153!=0         #15!=0                     #1!=0
    dig=num%10   #153%10=3        #15%10=5                  #1%10=1
    res=(res*10)+dig   #(0*10)+3=3      #(3*10)+5=35        #(35*10)+1=351
    num=num//10   #153//10=15          #15//10=1            #1//10=0
print(res)     #351