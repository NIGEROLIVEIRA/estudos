numero = int(input('Digite um numero entre 0 e 1000: '))

unidade = numero % 10
dezena = int((numero - unidade) / 10 % 10)
centena = int((((numero - unidade) / 10 ) - dezena) / 10)
print('Centena', centena, 'Dezena', dezena, 'Unidade', unidade)