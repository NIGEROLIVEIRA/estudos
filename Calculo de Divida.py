divida = int(input('Digite o valor total da sua divida:'))

print('Valor da Dívida      Valor dos Juros     Quantidade de Parcelas     Valor da Parcela')
loop = 0
lista =  [0, 10, 15, 20, 25]
for x in [1, 3, 6, 9, 12]:
    
    if loop >= 1:
        del lista[0]
    loop += 1
    for a in lista:
        juros = a
        break
    
    print('{0}                   {1}                  {2}                         {3} '.format(round(divida + (juros / 100) * divida), juros, x, round(divida / x, 2)))