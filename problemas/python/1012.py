x, y, z = input().split()
x, y, z = float(x), float(y), float(z)
at = x*z/2
ac = z**2*3.14159
atr = (x+y)*z/2
aq = y**2
ar = x*y
print(f'TRIANGULO: {at:.3f}')
print(f'CIRCULO: {ac:.3f}')
print(f'TRAPEZIO: {atr:.3f}')
print(f'QUADRADO: {aq:.3f}')
print(f'RETANGULO: {ar:.3f}')