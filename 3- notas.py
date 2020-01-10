
def entrada():
    notas = []
    for x in range(1, 5):
        numero = float(input('Digite o {0}° nota: '.format(x)))
        notas.append(numero)
    return notas

def soma():
    somando = 0
    for s in notas:
        somando += s
    return somando

notas = entrada()
media = soma()

print('\nA 1° Nota: {0}'.format(notas[0]))
print('A 2° Nota: {0}'.format(notas[1]))
print('A 3° Nota: {0}'.format(notas[2]))
print('A 4° Nota: {0}\n'.format(notas[3]))
print('A Nota Media {0}\n: '.format(media / 4))