x = int(input())
hora = int(x/3600)
novo1 = x - hora*3600
minuto = int(novo1/60)
novo2 = novo1 - minuto*60
segundo = novo2
print(f'{hora}:{minuto}:{segundo}')