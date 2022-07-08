#map function
#if each element has a corresponding output we use map function

#lst=[1,2,3,4,5,6,7,8,9,10]
#lst1=[]
#for i in lst:
#  if (i%2==0):
#      lst1.append(i)

#print(lst1)

lst=[1,2,3,4,5,6,7,8,9,10]
#def square(num):
#    res=num**2
#    return res

#data=list(map(square,lst))
#print(data)

#to avoid these many lines

data=list(map(lambda num:num*num,lst))
print(data)


