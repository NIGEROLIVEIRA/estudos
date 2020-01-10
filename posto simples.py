combustivel = input('Bem vindo ao Posto União! A = Alcool ou G= Gasolina: ')
litros = float(input('Quantos litros? '))

if combustivel == 'g' and litros <= 20:
    print('Total a pagar:', (litros * 2.50) - (4 / 100) * (litros * 2.50))

elif combustivel == 'g' and litros > 20:
    print('Total a pagar:', (litros * 2.50) - (6 / 100) * (litros * 2.50))

elif combustivel == 'a' and litros <= 20:
    print('Total a pagar:', (litros * 1.90) - (3 / 100) * (litros * 1.90))

elif combustivel == 'a' and litros > 20:
    print('Total a pagar:', (litros * 1.90) - (5 / 100) * (litros * 1.90))