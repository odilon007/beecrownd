codigo, quantidade = input().split()
codigo, quantidade = int(codigo), int(quantidade)
if codigo == 1:
    print(f'Total: R$ {4*quantidade:.2f}')
elif codigo == 2:
    print(f'Total: R$ {4.50*quantidade:.2f}')
elif codigo == 3:
    print(f'Total: R$ {5*quantidade:.2f}')
elif codigo == 4:
    print(f'Total: R$ {2*quantidade:.2f}')
elif codigo == 5:
    print(f'Total: R$ {1.5*quantidade:.2f}')

else:
    print('burro')