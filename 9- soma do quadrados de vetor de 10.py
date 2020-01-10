def multiplicacao():
    m = 0
    for x in lista:
        m += (x ** 2)
    return m
################################################
def entrada():
    lista = []
    for x in range(1, 5):
        numero = int(input('Digite o {0}° numero: '.format(x)))
        lista.append(numero)
    return lista
################################################
lista = entrada()
mul = multiplicacao()
print('A soma dos quadrados do vetor é: {0}'.format(mul))

