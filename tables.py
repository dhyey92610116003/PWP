num1=int(input("enter which table you want:"))
num2=int(input("enter the range of table:"))
mul=0
for i in range(1,num2+1):
    mul=num1*i
    # print(num1,"x",i,"=",mul)
    print(f"{num1} x {i} = {mul}")