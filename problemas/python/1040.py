n1, n2, n3, n4 = input().split()
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)
media = (n1*2+n2*3+n3*4+n4*1)/(2+3+4+1)
media = round(media, 1)
print(f'Media: {media:.1f}')
if media >= 7:
    print(f'Aluno aprovado.')
elif media < 5:
    print(f'Aluno reprovado.')
else:
    print('Aluno em exame.')
    ne = float(input())
    nota_exame = round(ne, 1)
    print(f'Nota do exame: {nota_exame:.1f}')
    nova_media = (media + nota_exame)/2
    if nova_media >= 5:
       print(f'Aluno aprovado.')
    else:
       print(f'Aluno reprovado.')
    print(f'Media final: {nova_media:.1f}')
