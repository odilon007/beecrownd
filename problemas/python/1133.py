soma = 0
num1 = int(input())
num2 = int(input())
if num1 < num2:
    num1, num2 = num2, num1
for i in range(num2+1, num1):
    if i % 5 == 2:
        print(i)
    elif i % 5 == 3:
        print(i)