#READ OPERATION

#read a file(sample1)


f=open("C:/Users/SuperUser/PycharmProjects/april_python/file_operations/sample1","r")
for i in f:
    print(i)

#          OR

#f=open("sample1","r")
#(but this is possible only if the file and the program are in the same package)
#for i in f:
#    print(i)