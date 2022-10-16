positivas = 0
numnotas = int(input("Introduza o número de notas: "))
for i in range(numnotas):
    if int(input(f"Introduza nota nº {i+1}: ")) >= 10: positivas += 1
print("Número de notas positivas:", positivas, "\nPercentagem de notas positivas:", positivas/numnotas*100, "%")