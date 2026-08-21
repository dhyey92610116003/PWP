x=int(input("Enter a number: "))

def factorial(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f

f=factorial(x)
print("Factorial of",x,"is",f)