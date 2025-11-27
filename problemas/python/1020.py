x = int(input())
ano = int(x/365)
novo1 = x - ano*365
mes = int(novo1/30)
novo2 = novo1 - mes*30
dias = novo2
print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')
