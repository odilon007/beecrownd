a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
if a == 0:
    print('Impossivel calcular')
else:
    raiz1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    raiz2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)
    if b**2-4*a*c < 0 or 2*a == 0:
        print('Impossivel calcular')
    else:
        print(f'R1 = {raiz1:.5f}')
        print(f'R2 = {raiz2:.5f}')