st={10,20,30,40,50,60,70,80,90,100}
print(st)

#REMOVE FUNCTION
#st.remove(30)
#print(st)

#DISCARD FUNCTION
#st.remove(30)
#print(st)

#****************************
#SET OPERATIONS
#1.union
#2.intersection
#3.difference

#1.union
st1={1,2,3,4,5,6,7}
st2={7,8,9,10,11,12,13,14}
#st1 union st2 {1,2,3,4,5,6,7,8,9,10,11,12,13,14

#st3=st1.union(st2)
#print(st3)

#2..intersection
st3=st1.intersection(st2)
print(st3)

#3difference
#A-B that is element in setA but not present in setB
#{1,2,3,4,5,6}
st3=st1.difference(st2)
print(st3)







