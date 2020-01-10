def entrada():
    vetor = []
    for x in range(1, 6):
        numero = int(input('Digite o {0}° numero inteiro: '.format(x)))
        vetor.append(numero)
    return vetor
########################################################################################
def multiplicacao():
    m = 1
    for x in vetor:
        m = (x * m)
    return m
########################################################################################

vetor = entrada()
mult = multiplicacao()

print('A soma do vetor de 5 é {0}'.format(sum(vetor)))
print('A multiplicaçao do vetor de 5 é {0}'.format(mult))