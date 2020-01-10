nun = int(input('Informe um numero Inteiro: '))
contador = 0
test = []
for y in range(1, nun + 1):

    for x in range(1, y + 1):
        if y % x == 0:
            contador += 1
    
    if contador <= 2:
        test.append(y)
    contador = 0
print('Foram verificados numeros de 1 ate {0}'.format(nun))
print('\n Apenas {0} são numeros primos! \n'.format(test))
exit()