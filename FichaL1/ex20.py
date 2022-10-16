primeiro = ''
for i in range(1,10):
    primeiro += str(i)
    resultado = int(primeiro) * 8 + i
    print(primeiro, "x 8 +", i, "=", resultado)
