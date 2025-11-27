while True:
    try:
        entrada = list(map(int, input().split()))
        a = entrada[0]
        for valor in entrada[1:]:
            if valor > 0:
                n = valor
                break
        else:
            while True:
                n = int(input())
                if n > 0:
                    break
        break
    except (ValueError, IndexError):
        print("Entrada inválida. Digite dois números (a e pelo menos um n > 0).")
soma = sum(a + i for i in range(n))
print(soma)
