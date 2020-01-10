print('Bem vindo a Fruteira! Promoção no Morango e na Maça. ')
morango = input('Quantos kilos de Morango você deseja comprar? ')
maca = input('Quantos kilos de Maça você deseja comprar? ')

if morango == '':
    morango = 0
elif maca == '':
    maca = 0

total = 0
while True:
    morango = float(morango)
    maca = float(maca)

    #verifica o preço com base nos kilos
    while morango > 0 and morango <= 5 and (morango + maca) <= 9:
            print('Preço do morango', morango * 2.50)
            total += morango * 2.50
            morango = 0
        
    
    while morango >5 and morango <= 8 and (morango + maca) <= 9:
            print('Preço do morango', morango * 2.20)
            total += morango * 2.20
            morango = 0
        
    while maca > 0 and maca <= 5 and (morango + maca) <= 9:
            print('Preço da maça', maca * 1.80)
            total += maca * 1.80
            maca = 0
        
    while maca > 5 and maca <= 8 and (morango + maca) <= 9:
            print('Preço da maça', maca * 1.50)
            total += maca * 1.50
            maca = 0
        
    #verifica se tem desconto de 10%
    while (morango + maca) >= 9:
        print('Total a pagar:', (morango * 2.20) + (maca * 1.50),'---------Parabens voçê ganhou "10%" de Desconto!')
        total = ((morango * 2.20) + (maca * 1.50) - (10 / 100 * ((morango * 2.20) + (maca * 1.50))))
        morango, maca = 0, 0

    print('Total a pagar', total)

    exit(0)