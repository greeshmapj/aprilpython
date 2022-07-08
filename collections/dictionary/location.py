#INTERVIEW

#str=(input("enter any word="))
#vowels='aeiou'
#str1=[]
#for i in str:
#    if i not in vowels:
#      print(i)

f=open("content","r")
spc='!@#$%^&*()'
for i in f:
   data=i.rstrip("\n")
   str=" "
   for j in data:
       if j not in spc:
           str+=j
   print(i)