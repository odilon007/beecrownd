x, y, z = map(float, input().split())
ordem = sorted([x, y, z], reverse=True)
a = ordem[0]
b = ordem[1]
c = ordem[2]
if a >= b+c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2+c**2:
        print('TRIANGULO RETANGULO')
    if a**2 > b**2+c**2:
        print('TRIANGULO OBTUSANGULO')
    if a**2 < b**2+c**2:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or c == b:
        print('TRIANGULO ISOSCELES')