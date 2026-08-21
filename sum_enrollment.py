# sum of digits of enrollment number using function

def enrollsum(x):   
    x=str(x)
    sum=0

    for i in x:
        i=int(i)
        sum=sum+i
    return sum

enrollsum(92610116003)
raj=enrollsum(92610116003)
print(raj)