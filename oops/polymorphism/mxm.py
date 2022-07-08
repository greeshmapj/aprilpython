lst=[('vinay',45),('arjun',56),('vipin',59),('anu',67)]
#print the name of the student with the highest mark
lst1=[]
for i in lst:
    lst1.append(i[1])

maximum=max(lst1)

for j in lst:
    if j[1]==maximum:
        print(j[0])