num_grenais = 0
vitorias_inter = 0
vitorias_gremio = 0
empate = 0
while True:
    inter, gremio = map(int, input().split())
    num_grenais += 1
    if inter == gremio:
        empate += 1
    elif inter > gremio:
        vitorias_inter += 1
    else: 
        vitorias_gremio += 1
    print('Novo grenal (1-sim 2-nao)')
    z = int(input())
    if z == 1:
        continue
    elif z == 2:
        break

print(f'{num_grenais} grenais')
print(f'Inter:{vitorias_inter}')
print(f'Gremio:{vitorias_gremio}')
print(f'Empates:{empate}')
if vitorias_inter > vitorias_gremio:
    print(f'Inter venceu mais')
elif vitorias_inter < vitorias_gremio:
    print(f'Gremio venceu mais')
else:
    print(f'Nao houve vencedor')

