dia1 = int(input().split()[1])
hora1 = list(map(int, input().split(':')))
dia2 = int(input().split()[1])
hora2 = list(map(int, input().split(':')))
segundos1 = dia1*86400 + hora1[0]*3600 + hora1[1]*60 + hora1[2]
segundos2 = dia2*86400 + hora2[0]*3600 + hora2[1]*60 + hora2[2]
total_segundos = abs(segundos1 - segundos2)
dias = total_segundos//86400
total_segundos %= 86400
horas = total_segundos//3600
total_segundos %= 3600
minutos = total_segundos//60
total_segundos %= 60
segundos = total_segundos
print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
