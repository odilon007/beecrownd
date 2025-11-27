while True:
    num1, num2 = map(int, input().split())
    if num1 > num2:
        print('Decrescente')
    if num1 < num2:
        print('Crescente')
    if num1 == num2:
        break