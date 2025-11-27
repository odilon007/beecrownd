x = int(input())
num1 = 1
num2 = 1
num3 = 1
temp = 1
for i in range(x):
    for j in range(2):
        print(num1, num2, num3)
        if j % 2 != 0:
            num2 += (1+i)*2
            num3 += 6*(temp) 
        else:
            num2 += 1
            num3 += 1
    num1 += 1
    temp += (i+2)
