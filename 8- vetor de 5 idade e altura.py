idade_lista = []

altura_lista = []

for x in range(1,3):
    idade = int(input('Digite a sua Idade: '))
    altura = float(input('Digite a sua Altura: '))
    idade_lista.append(idade)
    idade_lista.reverse()
    altura_lista.append(altura)
    altura_lista.reverse()

print('Idade: {}'.format(idade_lista))
print('altura: {}'.format(altura_lista))