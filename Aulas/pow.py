num1 = int(input("base: "))
num2 = int(input("expoente: "))

def mdc(m, n):
    while n != 0:
        resto = m % n
        m = n
        n = resto
    return m

def potencia(x, n):
    res = 1
    for i in range(abs(n)):
        res *= x
    if n < 0:
        return 1/res
    return res

def sqrt(x):
    p = 1
    while not verrt(x, p):
        p = (p + x/p) / 2
    return p
    

def verrt(x, estimate):
    if abs

print(potencia(num1, num2))
print(mdc(num1, num2))
