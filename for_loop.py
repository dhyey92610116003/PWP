# n1=[1,2,3,4,5]
# for i in n1:
#     print(i+1)

n2 = [9, 2, 6, 1, 0, 1, 1, 6, 0, 0, 3]

# Using [:] creates a fixed copy to loop through safely
for e in n2[:]:
    n2.append(2 * e)

print(n2)
# Output: [9, 2, 6, 1, 0, 1, 1, 6, 0, 0, 3, 18, 4, 12, 2, 0, 2, 2, 12, 0, 0, 6]
