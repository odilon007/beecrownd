x = float(input())
x = round(x, 2)
if 0<= x <= 400:
    NovoSalario = x*1.15
    print(f'Novo salario: {NovoSalario:.2f}')
    print(f'Reajuste ganho: {NovoSalario-x:.2f}')
    print(f'Em percentual: 15 %')
elif 400 < x <= 800:
    NovoSalario = x*1.12
    print(f'Novo salario: {NovoSalario:.2f}')
    print(f'Reajuste ganho: {NovoSalario-x:.2f}')
    print(f'Em percentual: 12 %')
elif 800 < x <= 1200:
    NovoSalario = x*1.1
    print(f'Novo salario: {NovoSalario:.2f}')
    print(f'Reajuste ganho: {NovoSalario-x:.2f}')
    print(f'Em percentual: 10 %')
elif 1200 < x <= 2000:
    NovoSalario = x*1.07
    print(f'Novo salario: {NovoSalario:.2f}')
    print(f'Reajuste ganho: {NovoSalario-x:.2f}')
    print(f'Em percentual: 7 %')
elif x > 2000:
    NovoSalario = x*1.04
    print(f'Novo salario: {NovoSalario:.2f}')
    print(f'Reajuste ganho: {NovoSalario-x:.2f}')
    print(f'Em percentual: 4 %')