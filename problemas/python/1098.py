i = 0
j = 1
while i <=2:
    while True:
        i = round(i, 1)
        if i %1 == 0:
            i = int(i)
        j = 1
        for _ in range(3):
            jnovo = j + i
            jnovo = round(jnovo, 1)
            if jnovo % 1 == 0:  
                jnovo = int(jnovo)
            print(f'I={i} J={jnovo}')
            j += 1
        break
    i += 0.2