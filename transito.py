maior_acidente = menor_acidente = acidente_smal_city = 0
codigo_a_maior = codigo_a_menor = 0
codigo_smal_city = 0
v = 0
loop = 1
cont = 1

def imprime():
    print('\n"Brasnorte-1"  "Juina-2"  "Juara-3"  "Campo Novo-4"  "Tangara-5" ')
    print('\nFoi feito a pesquisa com a media de {0} caros por cidades'.format(int(v / 5)))
    print('O maior indice pertence a cidade {0} com {1} acidentes'.format(codigo_a_maior, maior_acidente))
    print('O menor indice pertence a cidade {0} com {1} acidentes'.format(codigo_a_menor, menor_acidente))
    print('''Nas cidade  {0} que possui menos de 5000 carros foram registrados em media.
    {1} acidentes \n'''.format(codigo_smal_city, acidente_smal_city / cont))
    print(codigo_smal_city)
while loop <= 5:
    loop += 1
    #entradas de informaçao
    print('\n"Brasnorte-1"  "Juina-2"  "Juara-3"  "Campo Novo-4"  "Tangara-5" ')
    codigo  = list(input('\nInforme o Codigo da cidade: '))
    veiculo = int(input('Informe o numero de veiculo de passeio: '))
    acidente = int(input('Número de acidentes de trânsito com vítimas: '))
    v += veiculo
    #calcular acidentes. 
    if loop == 2:
        maior_acidente = menor_acidente = acidente
        codigo_smal_city = codigo

    elif acidente > maior_acidente:
        maior_acidente = acidente
        codigo_a_maior = codigo

    elif acidente < menor_acidente:
        menor_acidente = acidente 
        codigo_a_menor = codigo

    #calcular acidentes cidades pequenas.
    if veiculo < 5000:
        cont += 1
        codigo_smal_city = codigo
        acidente_smal_city += acidente
        
imprime()
exit()