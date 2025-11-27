x, y= map(int, input().split())
if y <= x:
    tempo = y+24-x
    print(f'O JOGO DUROU {tempo} HORA(S)')
else:
    tempo = abs(x-y)
    print(f'O JOGO DUROU {tempo} HORA(S)')