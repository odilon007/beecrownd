x = int(input())
cobaias = 0
coelhos = 0
ratos = 0
sapos = 0
for i in range(1, x+1):
    num_cobaia = input().split()
    cobaias += int(num_cobaia[0])
    if num_cobaia[1] == 'C':
        coelhos += int(num_cobaia[0])
    elif num_cobaia[1] == 'R':
        ratos += int(num_cobaia[0])
    elif num_cobaia[1] == 'S':
        sapos += int(num_cobaia[0])
percentual_co = coelhos/cobaias*100
percentual_ra = ratos/cobaias*100
percentual_sa = sapos/cobaias*100
print(f'Total: {cobaias} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {percentual_co:.2f} %')
print(f'Percentual de ratos: {percentual_ra:.2f} %')
print(f'Percentual de sapos: {percentual_sa:.2f} %')