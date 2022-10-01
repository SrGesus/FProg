string = input("Introduz o número inteiro: ")
count = 0
for i in range(len(string)):
    if string[i] == '0' and i + 1 < len(string) and string[i+1] == '0':
        count += 1
print(count)
