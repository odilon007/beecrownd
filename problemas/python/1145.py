x, y = map(int, input().split())
numero_atual = 1
for i in range(1, y+1):
    print(numero_atual, end="")
    if i % x != 0:
        print(' ', end="")
    else:
        print()
    numero_atual += 1