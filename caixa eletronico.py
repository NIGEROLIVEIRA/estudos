import sys
saque = int(input('Qual valor você deseja sacar: '))
#valor saque nao permitido.
if saque > 600 or saque < 10:
    print('Limite maximo 600 e minimo 10')
    sys.exit()
total = saque
cedula = 100
totalcedula = 0
while True:
    if saque >= cedula:
        saque -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print('Total de', totalcedula, ' cédulas de R$', cedula,'...[OK]')
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        totalcedula = 0 
        if saque == 0:
            print('Transação realizada com sucesso!\nSaque no valor total de => : R$', total)
            exit()
