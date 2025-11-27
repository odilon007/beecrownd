i = 1
j = 7
while True:
    for _ in range(3):
        print(f'I={i} J={j}')
        j -= 1
    i += 2
    j += 5
    if i > 9:
        break
    