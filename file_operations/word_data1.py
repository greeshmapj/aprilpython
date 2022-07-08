#read the word_data file and do the word count

f=open("word_data","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(" ")

    for i in data:
        if i not in dic:
           dic[i]=1
        else:
           dic[i]+=1
print(dic)

for i in dic:
    print(i,",",dic[i])