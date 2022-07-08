master_string="abbcddeghgggt"
chik_word="egg"    #form this

res=""

wc={}
for char in master_string:
    if char in wc:
        wc[char]+=1
    else:
        wc[char]=1

for char in chik_word:
    if char in wc:
        curCount=wc.get(char)
        if curCount>0:
            res+=char
            wc[char]-=1
        else:
            break
    else:
        break
print(res==chik_word)
