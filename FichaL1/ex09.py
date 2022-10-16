resultado = ''
while True:
    digito = input("Introduza um dígito (-1 para terminar)\n? ")
    if digito == '-1':
        break
    resultado += digito
print(resultado)
