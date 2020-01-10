print(25 * '#')
print('Tela de login')
nome = input('Usuario: ')
senha = input('Senha: ')
while True:
    while nome == senha:
        print('Nome e Senha iguais não são permitidos. Informe novamente seu usuario e senha.')
        nome = input('Usuario: ')
        senha = input('Senha: ')
    else:
        print('Usuario e senha validado com sucesso!')
    exit(0)