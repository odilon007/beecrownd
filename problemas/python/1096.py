ii = 1
j = 7
print(f'I={ii} J={j}')
print(f'I={ii} J={j-1}')
print(f'I={ii} J={j-2}')
for i in range(4):
    ii += 2
    if ii + 2:
        for i in range(3):
            print(f'I={ii} J={j}')
            j -= 1
    j = 7