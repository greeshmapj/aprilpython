#for checking 3 or more conditions

#if
#elif
#else

#syntax

#cost price of bike

cost=int(input("enter the cost price="))
tax=0
if(cost>100000):
    print("tax=",0.15*cost)
elif(50000<cost<=100000):
    print("tax=",0.10*cost)
elif(cost<=50000):
    print("tax=",0.05*cost)
else:
    print("not applicable")
