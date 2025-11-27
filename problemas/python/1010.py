cod1, num1, valor1 = input().split()
cod1 = int(cod1)
num1 = int(num1)
valor1 = float(valor1)
cod2, num2, valor2 = input().split()
cod2 = int(cod2)
num2 = int(num2)
valor2 = float(valor2)
total = (num1*valor1) + (num2*valor2)
print(f'VALOR A PAGAR: R$ {total:.2f}')



