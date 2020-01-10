salario = int(input('Digite o seu salario atual: '))

if salario <= 280:
    print('O salário antes do reajuste:',salario, 'R$')
    print('O percentual de aumento aplicado: 20%')
    print('O valor do aumento: ', ((20 / 100) * salario), 'R$')
    print('O novo salário, após o aumento: ', ((20 / 100) * salario + salario), 'R$')
elif salario > 280 and salario < 700:
    print('O salário antes do reajuste:',salario, 'R$')
    print('O percentual de aumento aplicado: 15%')
    print('O valor do aumento: ', ((15 / 100) * salario), 'R$')
    print('O novo salário, após o aumento: ', ((15 / 100) * salario + salario), 'R$')
elif salario > 700 and salario < 1500:
    print('O salário antes do reajuste:',salario, 'R$')
    print('O percentual de aumento aplicado: 10%')
    print('O valor do aumento: ', ((10 / 100) * salario), 'R$')
    print('O novo salário, após o aumento: ', ((10 / 100) * salario + salario), 'R$')
elif salario > 1500:
    print('O salário antes do reajuste:',salario, 'R$')
    print('O percentual de aumento aplicado: 5%')
    print('O valor do aumento: ', ((5 / 100) * salario), 'R$')
    print('O novo salário, após o aumento: ', ((5 / 100) * salario + salario), 'R$')