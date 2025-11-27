x, y, z = input().split()
x, y, z = int(x), int(y), int(z)
maiorxyz = ((x+y)+abs(x-y))/2
if z > maiorxyz:
    maiorxyz = z
print(f'{maiorxyz:.0f} eh o maior')