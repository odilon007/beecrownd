x = int(input())
y = int(input())
soma = 0
if x > y and y%2 != 0:
    for i in range(y+2, x, 2):
        soma += i
elif x > y and y%2 == 0:
    for i in range(y+1, x, 2):
        soma += i
if x < y and y%2 != 0:
    for i in range(y+2, x, 2):
        soma += i
if x < y and y%2 == 0:
    for i in range(y+1, x, 2):
        soma += i
print(soma)