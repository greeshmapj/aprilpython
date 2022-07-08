tu=(30,45,50,55,60,65,70,75,80)
print(tu)
#convert tu50 to 100
#so we convert tuple to list and mutate it and change it back to tu

lst=list(tu)
print(lst)
lst[2]=100
print(lst)
tu=tuple(lst)
print(tu)


