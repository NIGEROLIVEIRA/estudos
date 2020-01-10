eleitor = int(input('Qual o total de eleitores: '))
joao = int(0)
lula = int(0)
bolsonaro = int(0)
idadem = int(0)
a = 0
for x in range(eleitor):
    voto = int(input('JOÃO 14, LULA 13, BOLSONARO 17 :'))
    a += 1
    if voto == 14:
        joao += 1

    elif voto == 13:
        lula += 1
    
    elif voto == 17:
        bolsonaro += 1
print('De {0} eleitores que votaram {1}% em JOÃO {2}% em LULA e {3}% em Bolsonaro'.format(a, (joao / a) * 100, (lula / a) * 100, (bolsonaro / a) * 100))
exit()    