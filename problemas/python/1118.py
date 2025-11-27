while True:
    # Primeira nota
    while True:
        x = float(input())
        if 0 <= x <= 10:
            break
        else:
            print('nota invalida')

    # Segunda nota
    while True:
        y = float(input())
        if 0 <= y <= 10:
            break
        else:
            print('nota invalida')

    media = (x + y) / 2
    print(f'media = {media:.2f}')

    # Novo cálculo
    while True:
        print('novo calculo (1-sim 2-nao)')
        verf = int(input())
        if verf == 1:
            break  # Faz novo cálculo
        elif verf == 2:
            exit()  # Sai do programa