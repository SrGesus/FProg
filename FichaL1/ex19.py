quantia, notas = float(input("Introduz a quantia: ")) * 100, [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
for i in range(len(notas)):
    print(notas[i], "€:\t", int(quantia // (notas[i] * 100)))
    quantia -= (quantia // (notas[i] * 100)) * (notas[i] * 100)