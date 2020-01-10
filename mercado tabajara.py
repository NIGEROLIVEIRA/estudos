print('Bem vindo ao Mercado Pasqualoto! Promoção de carne. File Duplo, Alcatra, Picanha. ')
carne = input('Qual tipo de carne voçê deseja comprar? ')
kg = float(input('Quantos kilos de você quer? '))
pagar = input('Como deseja pagar? "Cartão", "Dinheiro" ou "Cheque"? ')
total = 0
while True:
    #verifica qual o tipo de carne com base na var carne.
#################################################################
    while carne == 'file' or carne == 'duplo' or carne == 'file duplo' and kg > 0 and kg <= 5:
            print('Preço do File Duplo', kg * 4.90,'R$')
            carne , kg, total = 0, 0, kg * 4.90
    while carne == 'file' or carne == 'duplo' or carne == 'file duplo' and kg > 5:
            print('Preço do File Duplo', kg * 5.80,'R$')
            carne , kg, total = 0, 0, kg * 5.80
##################################################################      
    while carne == 'Alcatra' or carne == 'alcatra' or carne == 'ALCATRA' and kg > 0 and kg <= 5:
            print('Preço da Alcatra', kg * 5.90,'R$')
            carne , kg, total = 0, 0, kg * 5.90
    while carne == 'Alcatra' or carne == 'alcatra' or carne == 'ALCATRA' and kg > 5:
            print('Preço da Alcatra', kg * 6.80,'R$')
            carne , kg, total = 0, 0, kg * 6.80
##################################################################     
    while carne == 'Picanha' or carne == 'picanha' or carne == 'PICANHA' and kg > 0 and kg <= 5:
            print('Preço da Picanha', kg * 6.90,'R$')
            carne , kg, total = 0, 0, kg * 6.90
    while carne == 'Picanha' or carne == 'picanha' or carne == 'PICANHA' and kg > 5:
            print('Preço da Picanha', kg * 7.80,'R$')
            carne , kg, total = 0, 0, kg * 7.80
###################################################################
    if pagar == 'cartao':
        print('Total a pagar com desconto:', total - (5 / 100) * total,'R$')
    elif pagar == 'dinheiro' or 'cheque':
        print('Total a pagar:', total,'R$')

    exit(0)