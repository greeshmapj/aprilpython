lst=[1,2,3,4,5]
try:
    print(lst[6])
except:
    print("index out of range")
finally:
    print("inside")