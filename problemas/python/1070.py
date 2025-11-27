num1 = int(input())
if num1 % 2 != 0:
    for i in range(num1, num1+11, 2):
        print(i)
else:
    for i in range(num1+1, num1+13, 2):
        print(i)