num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
lista = [num1, num2, num3, num4, num5]
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in lista:
    if i % 2 == 0:
        pares += 1
    if i % 2 != 0:
        impares += 1
    if i > 0:
        positivos += 1
    if i < 0:
        negativos += 1
print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')