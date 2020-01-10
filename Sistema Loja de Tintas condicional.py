metros = float(input('Qua a area em metros quadrados você de seja pintar? '))
tinta = metros / 6
lata18 = tinta / 18
lata3 = tinta / 3.6
if metros >= 70:
    print('Você gastara ', lata18, 'Lata de tinta 18L.')
    print('Valor da compra ',tinta * (80 / 18), 'R$')
elif metros < 70:
    print('Você gastara ', lata3, 'Lata de tinta 3.6L.')
    print('Valor da compra ',tinta * (25 / 3.6), 'R$')