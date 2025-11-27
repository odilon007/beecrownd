x, a, y, b = map(int, input().split())
inicio = x*60+a
fim = y*60+b
if fim <= inicio:
    fim += 24*60
duracao = fim - inicio
horas = duracao//60
minutos = duracao%60
print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')