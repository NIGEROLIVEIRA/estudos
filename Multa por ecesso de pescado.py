peixe = float(input('Quantos quilos de pescado: '))
if peixe > 50:
    peso = (peixe - 50) * 4
    print('Multa por ecesso de peso: ', peso,'R$')
else:
    print('Tudo certo nao foi gerado multa')