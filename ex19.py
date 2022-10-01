quantia = float(input("Introduz a quantia: "))
notas = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
for i in range(len(notas)):
    num = quantia // notas[i] 
    quantia -= num * notas[i]
    print(notas[i], "€:\t", int(num))
