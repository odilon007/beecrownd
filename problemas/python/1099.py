n = int(input())
for i in range(n):
    num1, num2 = map(int, input().split())
    soma = 0
    while num1 < num2 and num1 % 2 == 1:
        num1 += 2
        if num1 >= num2:
            break
        soma += num1
    while num1 < num2 and num1 % 2 == 0:
        num1 += 1
        if num1 >= num2:
            break
        soma += num1
        num1 += 1
    while num1 > num2 and num2 % 2 == 1:
        num2 += 2
        if num2 >= num1:
            break
        soma += num2
    while num1 > num2 and num2 % 2 == 0:
        num2 += 1
        if num2 >= num1:
            break
        soma += num2
        num2 += 1
    print(soma)
        