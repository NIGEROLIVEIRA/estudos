def km():
    mildic = {}
    millista = []
    for x in carro.keys():
        calculo = 1000 / carro.get(x)
        millista.append(calculo)
        mildic [calculo] = x
        print('\n{1} \n{0}L para percorer 1000km'.format(round(calculo, 2), x))
        print('{0} gastaria {1}R$ para percorer 1000km'.format(x, round(calculo * 2.25)))
    millista.sort()
    print('\nO menor consumo é do {}'.format(mildic.get(millista[0])))



carro = {'Fusca':12, 'Voyage':11, 'Uno':19, 'Prisma':13, 'Siena':15}
km()

