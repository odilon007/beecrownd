senha = {
    2002:'Acesso Permitido'
}
while True:
    x = int(input())
    if x in senha:
        print(senha[x])
        break
    else:
        print('Senha Invalida')