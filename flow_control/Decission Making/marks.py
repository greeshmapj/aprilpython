#marks  4 subject marks out of 50

#above 180 A+
#160-179 A
#140-159 B+
#120-139 B
#100-119 C+
#80-99 C
# failed

sub1=int(input("enter marks of sub1"))
sub2=int(input("enter marks of sub2"))
sub3=int(input("enter marks of sub3"))
sub4=int(input("enter marks of sub4"))
marks=(sub1+sub2+sub3+sub4)
print(marks)

if(marks>=180):
    print("A+")
elif(160<=marks<=179):
    print("A")
elif(140<=marks<=159):
    print("B+")
elif(120<=marks<=139):
    print("C")
else:
    print("failed")