def calcular_notas(valor: float) -> dict:
    notas = {}
    notas[100] = valor//100
    valor %= 100
    notas[50] = valor//50
    valor %= 50
    notas[20] = valor//20
    valor %= 20
    notas[10] = valor//10
    valor %= 10
    notas[5] = valor//5
    valor %= 5
    notas[2] = valor//2
    valor = int(valor%2)
    return notas, valor

def calcular_moedas(valor: float) -> dict:
    moedas = {}
    centavos = round(valor * 100)
    moedas[100] = centavos // 100
    centavos %= 100
    moedas[50] = centavos // 50
    centavos %= 50
    moedas[25] = centavos // 25
    centavos %= 25
    moedas[10] = centavos // 10
    centavos %= 10
    moedas[5] = centavos // 5
    centavos %= 5
    moedas[1] = centavos // 1
    return moedas

valor_total = float(input())
parte_inteira = int(valor_total)
parte_decimal = valor_total - parte_inteira
resultado_notas, sobra_reais = calcular_notas(valor_total)
print('NOTAS:')
for notas, quantidade in resultado_notas.items():
    print(f'{quantidade:.0f} nota(s) de R$ {notas:.2f}')
total_centavos = round((sobra_reais + parte_decimal)*100)/100
resultado_moedas = calcular_moedas(total_centavos)
print('MOEDAS:')
for moedas, quantidade in resultado_moedas.items():
    print(f'{quantidade:.0f} moeda(s) de R$ {moedas/100:.2f}')