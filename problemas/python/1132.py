soma = 0
num1 = int(input())
num2 = int(input())
if num1 < num2:
    num1, num2 = num2, num1
for i in range(num2, num1+1):
    if i % 13 != 0:
        soma += i
print(soma)