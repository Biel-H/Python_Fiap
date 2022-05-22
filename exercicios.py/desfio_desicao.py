# O módulo solicitará o nivel de acesso de uma pessoa que pode ser : ADM, USR ou GUEST e o gênero dessa pessoa, caso o nível for USR, deverá exibir 'OLÁ USUÁRIO' para os homens ou 'Olá administradoras para as mulheres'.
#Se o nível for USR, deverá exibir "Olá usuário" para os omens ou Olá usuária para as mulheres.
#Se o nível foi GUEST, deverá exibir "Olá desconhecido(a)", considere apenas os gêneros masculino e feminino.

print(8 * '=~', " Seja bem vindo ao nosso programa ", 8 * '=~')
nome = input('Por favor nos informe seu nome: ')
sexo = input('Por favor nos infomre seu sexo (H,M): ').upper()
acesso = input('Por fim nos informa seu nível de acesso: ').upper()
if acesso == 'ADM':
    if sexo == 'H':
        print('Olá admnistrador!')
    else:
        print('Olá administradora!')
elif acesso=='USR':
    if sexo == 'H':
        print('Olá usuário!')
    else:
        print('Olá usuária!')
elif acesso == 'GUEST':
        print('Olá visitante!')
else:
    print('Olá desconhecido(a)!')

