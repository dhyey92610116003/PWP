number1=int(input("enter your enrollment number:"))
z=str(number1)
mul=1
for i in z:
    if i != '0':
        mul *= int(i)
print(mul)
