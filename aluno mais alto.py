alu = altu = altum = alun = alum = 0
cont = 0
for x in range(5):
    cont += 1
    alu = int(input('Qual o numero do aluno: '))
    alt = int(input('Qual a sua altura: '))

    if cont == 1:
        altum = altu = alt
        alum = alun = alu

    if alt > altu:
        altu = alt
        alun = alu
    elif alt < altum:
        altum = alt
        alum = alu


print('O aluno {0} é o maior com {1} cm.'.format(alu, altu))
print('O aluno {0} é o menor com {1} cm.'.format(alum, altum))
exit()