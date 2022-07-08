#lst=[1,2,3,4,5,6,7,8,9,10]
#add 1 to element [2,3,4,5,6,7,8,9,..]

#data=list(map(lambda num:num+1,lst))
#print(data)


#LIST COMPREHENSION
#lst=[]
#for i in range(1,101):
#    lst.append(i)
#print(lst)


#for the range of 1 to 75 make a list (1,5,9,13,17,21...)

#lst=[i for i in range(1,51) if i%2==1]
#print(lst)

#lst=[i**2 if i%2==0 else 0 if i%5==0 else i for i in range(1,31) ]
#print(lst)

#lst=[i if ('a','e','i','o','u') for i in range('luminartechnolab')]



name='luminartechnolab'
vowels='aeiou'


lst=['y' if i in vowels else 'n' for i in name]
print(lst)