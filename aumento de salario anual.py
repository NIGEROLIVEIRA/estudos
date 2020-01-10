salario = float(input('Informe o salario atual: '))
ano = int(input('Quantos anos voce trabalha nesta empresa: '))
p = 0
loop = 0

for x in range(1, ano + 1):
    loop += 1
    if loop == 1:
        salario = salario
    else:
        salario += (p / 100) * salario
###############################################
#porcentagem
    if loop == 1:
        p = 1.5
    else:
        p = p * 2

print('salario atual é {0}'.format(round(salario, 2)))
exit()