string = input("Introduza um número inteiro: ")
result = ''
for i in string:
    if int(i) % 2:
        result += i
print(result)
