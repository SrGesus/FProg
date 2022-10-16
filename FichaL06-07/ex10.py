def codifica(texto):
    return ''.join([texto[i] for i in range(0, len(texto), 2)] + [texto[i] for i in range(1, len(texto), 2)])

def descodifica(texto):
    return ''.join([texto[i//2] if i % 2 == 0 else texto[(len(texto)+i)//2] for i in range(0, len(texto))])

print(codifica('abcde'))
print(descodifica(codifica('era uma vez um gato maltes')))