def entrada():
    vetor = []
    for x in range(1, 6):
        numero = int(input('Digite o {0}° numero inteiro: '.format(x)))
        vetor.append(numero)
    return vetor

vetor = entrada()
print('vetor de [5] = ', vetor)