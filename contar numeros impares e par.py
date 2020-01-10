
par = impar = 0

while (par + impar) < 10:
    numero = input('Digite um numero inteiro: ')
    while numero == '':#verifica se o input esta  vasio e pede um numero
        numero = input('Digite um numero inteiro: ')
    
    if int(numero) % 2 == 0:
        print('numero "Par"')
        par += 1
    else:
        print('numero "Impar"')
        impar += 1

print('Total de numero Impar {0}. Total de numero par {1}'.format(impar, par))
exit()