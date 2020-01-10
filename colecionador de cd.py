cds = int(input('Quantos cd você adiquiriu: '))
prem = int(0)
for x in range(cds):
    preco = int(input('Qual o preço você pagou no {0}° CD: '.format(x + 1)))
    if preco > 0:
        prem = preco + prem
print('Voçê comprou {1} Cd. Em media você pagou {0} R$ por CD.'.format((prem / cds), cds))
exit()