x, y, z = map(float, input().split())
if x+y > z and x+z > y and y+z > x:
	perimetro = x+y+z
	print(f'Perimetro = {perimetro:.1f}')
else:
	area = (x+y)*z/2
	print(f'Area = {area:.1f}')