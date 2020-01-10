quantidade = int(input('Quantos itens voce vai comprar: '))
preco = float(input('Qual o preço da tabela fixa atualmente: '))
print('Lojas Quase Dois - Tabela de preços')
for x in range(1, quantidade + 1):
    print('{0} - R$ {1} R$'.format((x), (preco * x)))

exit()
