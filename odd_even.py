enroll=92610116003
e1=[]
d1=[]
a=0
x=str(enroll)
for i in x:
    a=int(i)
    if a%2==0:
        e1.append(a)
        
    else:
        d1.append(a)
print("even numbers are:",e1)
print("odd numbers are:",d1)
