#claculate the sum

def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(sum(4,6,7,8,9))
