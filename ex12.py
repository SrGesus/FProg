x = int(input("x: "))
n = int(input("n: "))
element = 1
result = 1
for i in range(n):
    element *= x / (i+1)
    result += element
print(result)
