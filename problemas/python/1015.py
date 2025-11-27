def distancia_dois_pontos(a: float, b: float,c: float ,d: float) -> float:
	return ((c-a)**2 + (d-b)**2)**(1/2)

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
resultado = distancia_dois_pontos(x1,y1,x2,y2)
print(f'{resultado:.4f}')