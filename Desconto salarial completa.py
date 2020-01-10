hora = int(input('Digite quantas horas você trabalha: '))
valor = float(input('Digite qual o valor da sua hora: '))
salario = hora * valor
inss = (10 / 100) * salario
fgts = (11 / 100) * salario
#imprime salario bruto.
print('Salario bruto: ', salario, 'R$')
# if para achar a porcentagem de desconto do IR.
if salario <= 900:
    print('Desconto   IR = Isento')
elif salario > 900 and salario <= 1500:
    print('Desconto   IR =', (5 / 100) * salario, 'R$----------[5%]')
elif salario > 1500 and salario < 2500:
    print('Desconto   IR =', (10 / 100) * salario, 'R$---------[10%]')
elif salario > 2500:
    print('Desconto   IR =', (20 / 100) * salario, 'R$---------[20%]')
#desconto do inss.
print('Desconto INSS =', ((10 / 100) * salario), 'R$--------[10%]')
#desconto FGTS.
print('Desconto FGTS =', fgts ,'R$--------[11%]')
#total de descontos.
if salario <= 900:
    print('Desconto Total =', (inss), 'R$--------[10%]')
elif salario > 900 and salario <= 1500:
    print('Desconto Total =', (((5 / 100) * salario + inss)), 'R$--------[15%]')
elif salario > 1500 and salario < 2500:
    print('Desconto Total =', (((10 / 100) * salario + inss)), 'R$---------[20%]')
elif salario > 2500:
    print('Desconto Total =', (((20 / 100) * salario + inss)), 'R$---------[30%]')
#salario liquido apos descontos.
if salario <= 900:
    print('Salario Liquido =', salario - inss, 'R$')

elif salario > 900 and salario <= 1500:
    print('Salario Liquido =', (salario-((5 / 100) * salario + inss)), 'R$')

elif salario > 1500 and salario < 2500:
    print('Salario Liquido =', (salario - ((10 / 100) * salario + inss)), 'R$')

elif salario > 2500:
    print('Salario Liquido =', (salario - ((20 / 100) * salario + inss)), 'R$')