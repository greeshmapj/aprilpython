#A company decide to give bonus of 5% to employee if his/her year of service is more than 5 years.
#ask user for their salary and year of service and print the net bonus amount.

salary=float(input("enter salary="))
experience=int(input("years of service="))

if(experience>5):
    print("bonus=",salary*0.05)
else:
    print("not eligible")
