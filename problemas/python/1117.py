while True:
    num1 = float(input())
    num2 = float(input())
    while num1 < 0 or num1 > 10:
        print('nota invalida')
        num1 = float(input())
    while num2 < 0 or num2 > 10:
        print('nota invalida')
        num2 = float(input())
    else:
        media = (num1 + num2)/2
        print(f'media = {media:.2f}')
        break