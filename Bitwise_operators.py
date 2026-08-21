n1=9
n2=3
print(bin(n1))
print(bin(n2))

x=5
y=3
print(format(x,"04b"))
print(format(y,"04b"))

result=x&y
print("Bitwise AND:",result)

rsult=x|y
print("Bitwise OR:",rsult)

result=x^y
print("Bitwise XOR:",result)

leftshift=x<<1
print("Left Shift:",leftshift)

rightshift=x>>1
print("Right Shift:",rightshift)