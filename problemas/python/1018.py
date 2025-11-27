x = int(input())
cem = int(x/100)
novo1 = x-cem*100
cinquenta = int(novo1/50)
novo2 = novo1 - cinquenta*50
vinte = int(novo2/20)
novo3 = novo2 - vinte*20
dez = int(novo3/10)
novo4 = novo3 - dez*10
cinco = int(novo4/5)
novo5 = novo4 - cinco*5
dois = int(novo5/2)
novo6 = novo5 - dois*2
um = int(novo6/1)
print(x)
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')