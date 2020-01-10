def entrada():
    vetor = []
    for x in range(1, 11):
        numero = int(input('Digite o {0}° numero inteiro: '.format(x)))
        vetor.append(numero)
    vetor.reverse()
    return vetor

vetor = entrada()
print('vetor de [10] = ', vetor)