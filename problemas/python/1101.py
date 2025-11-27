while  True:
    num1, num2 = map(int, input().split())
    if num1 > num2:
        num1, num2 = num2, num1

    if num1 > 0 and num2 > 0:
        numeros = list(range(num1, num2 + 1))
        soma = sum(numeros)
        print(f"{' '.join(str(x) for x in numeros)} Sum={sum(numeros)}")
    else:
        break