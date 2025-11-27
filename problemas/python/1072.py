n = int(input())
valores = []
in_ = 0
out = 0
for i in range(n):
    x = int(input())
    valores.append(x)
for i in valores:
    if 10 <= i <= 20:
        in_ += 1
    else:
        out += 1
print(f'{in_} in')
print(f'{out} out')