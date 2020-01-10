altura = float(input('Qual é a sua altura: '))
sexo = input('Qual é o seu sexo: ')
if sexo == 'masculino':
    pesoIdeal = 72.7 * altura - 58
    print('O seu peso ideal é: ',pesoIdeal)
elif sexo == 'feminino':
    pesoIdeal = 62.1 * altura - 44.7
    print('O seu peso ideal é: ',pesoIdeal)