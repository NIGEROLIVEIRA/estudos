preço1 = float(input('Digite o preço bombom garoto: '))
preço2 = float(input('Digite o preço bombom chocolate: '))
preço3 = float(input('Digite o preço bombom granola: '))

if preço1 < preço2:
    print('bombom garoto é mais Barato')

elif preço2 > preço3:
    print('bombom chocolate é mais barato')
else:
    print('bombom granola é mais barato')