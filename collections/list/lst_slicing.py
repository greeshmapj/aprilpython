#LIST SLICING

lst=[10,15,20,9,45,60,78]

#index
#POSITIVE INDEXING
print(lst[1:4])      #lst[1],lst[2],lst[3]         15,20,9

print(lst[3:8])      #lst[3],lst[4],lst[5],lst[6],lst[7]

print(lst[4:9])      #lst[4],lst[5],lst[6],lst[7],lst[8]

print(lst[:7])  #lst[0],lst[1],lst[2],............lst[6]

print(lst[:])    #entire elements

print(lst[3:])       #lst[3] to end

#NEGATIVE INDEXING
#[-1 TO -n]

print(lst[-1])   #78
print(lst[-3])   #45
print(lst[-5])   #20

print(lst[-4:-1])  #lst[-4] lst[-3] lst[-2]  [ 9,45,60]

