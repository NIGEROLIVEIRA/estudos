resposta = 's'
while resposta == 's':
    nun = int(input('Digite um numero inteiro entre 0 e 16: '))
    if nun < 0 or nun > 16:
        print('Valor incorreto!')
        exit()
    fat = ''
    fatorial = nun
    total = nun
    while nun > 1:
        nun -= 1
        fatorial = nun * fatorial
        fat += 'x' + str(nun)
    print('O fatorial de {0} é {1}'.format(total, fatorial))
    print('{0} != {0}{1}'.format(total, fat))
    resposta = input('Deseja fazer outro calculo? S/N:')
exit()
