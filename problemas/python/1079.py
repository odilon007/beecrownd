n = int(input())
for i in range(n):
    m1, m2, m3 = map(float, input().split())
    media = (m1*2+m2*3+m3*5)/10
    print(f'{media:.1f}')