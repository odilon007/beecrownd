n = int(input())
valores = []
for i in range(n):
    x = int(input())
    valores.append(x)
for x in valores:
    if x == 0:
        print('NULL')
    elif x % 2 == 0 and x>0:
        print('EVEN POSITIVE')
    elif x % 2 == 0 and x<0:
        print('EVEN NEGATIVE')
    elif x % 2 != 0 and x>0:
        print('ODD POSITIVE')
    elif x % 2 != 0 and x<0:
        print('ODD NEGATIVE')