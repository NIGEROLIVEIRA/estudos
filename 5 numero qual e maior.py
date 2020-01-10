maior, menor, inp, loop = 0, 0, 0, 0
while loop < 5:
    loop += 1
    inp = int(input('Digite um numero entre 0 e 1000: '))
    if inp < 0 or inp > 1000:
        print('Numero fora do parametro')
        exit()
    if loop == 1:
        maior, menor = inp, inp #armazena o valor de inp dentro de maior e menor no primeiroloop de repetiçao.
    else:
        if inp > maior:
            maior = inp
        elif inp < menor:
            menor = inp    
print('O numero maior é: ', maior, 'e o numero menor é ', menor)
print('A soma do maior e do menor é ', maior + menor)
exit(0)
