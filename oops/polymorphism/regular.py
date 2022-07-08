import re
s="vavavavavavavvvvaaa"
count=0
matcher=re.finditer('av',s)
for i in matcher:
    count+=1
    print(i.start())
    print(i.group())
print(count)