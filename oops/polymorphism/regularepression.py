import re
s="abaaaabbbbbbbbbbaaaaaaaaaaa"
count=0
#finditer(a function is our regular epression,'re')
    #finditer(argument,argument2)
#argument1:find pattern
#argument2:the name of the string with with the matching is checked

#we have to find the no. of times ab found in pattern
matcher=re.finditer('ab',s)           #matcher=variable name
#print(matcher)  error.....only the location will be output
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)



