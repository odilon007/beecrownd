num1 = float(input())
if 0 <= num1 <= 25:
    print('Intervalo [0,25]')
elif 25 < num1 <= 50:
    print('Intervalo (25,50]')
elif 50 < num1 <= 75:
    print('Intervalo (50,75]')
elif 75 < num1 <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')