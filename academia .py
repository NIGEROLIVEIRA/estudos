maioraltura = menoraltura = maiorpeso = menorpeso = 0
codigo_a_maior = codigo_a_menor = codigo_p_maior = codigo_p_menor = 0
peso_maior = peso_menor = alt_maior = alt_menor = 0

loop = 0
def imprime():
    print('maior Altura codigo:{0} com {1} metros e pesando {2}Kg'.format(codigo_a_maior, maioraltura, peso_maior))
    print('Menor Altura codigo:{0} com {1} metros e pesando {2}Kg'.format(codigo_a_menor, menoraltura, peso_menor))
    print('Maior Peso   codigo:{0} com {1} metros e pesando {2}Kg'.format(codigo_p_maior, alt_maior, maiorpeso))
    print('Menor Peso   codigo:{0} com {1} metros e pesando {2}Kg'.format(codigo_p_menor, alt_menor, menorpeso))

while True:
    loop += 1

    codigo  = int(input('Informe o seu codigo: '))
    if codigo == 0:
        imprime()
        exit()

    altura = float(input('Informe a sua altura: '))
    peso = float(input('Informe a seu peso: '))
    
    #calcular altura. 
    if loop == 1:
        maioraltura = menoraltura = altura

    elif altura > maioraltura:
        maioraltura = altura
        codigo_a_maior = codigo
        peso_maior = peso

    elif altura < menoraltura:
        menoraltura = altura 
        codigo_a_menor = codigo
        peso_menor = peso

    #calcular peso.
    if loop == 1:
        maiorpeso = menorpeso = peso

    elif peso > maiorpeso:
        maiorpeso = peso
        codigo_p_maior = codigo
        alt_maior = altura

    elif peso < menorpeso:
        menorpeso = peso
        codigo_p_menor = codigo
        alt_menor = altura

exit()