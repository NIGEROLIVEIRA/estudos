num1 = float(input('Digite o primeiro numero para calcular: '))
operador = input('Digite o operado que deseja usar: + - * / ')
num2 = float(input('Digite o segundo numero para calcular: '))


while True:

    if operador == '+':
        calculo = num1 + num2

    elif operador == '-':
        calculo = num1 - num2
    
    elif operador == '*':
        calculo = num1 * num2

    elif operador == '/':
        calculo = num1 / num2

    print(calculo)
    # par ou impar
    parimpar = calculo % 2 
    if parimpar == 0:
        print(calculo, 'é Par')
    else:
        print(calculo, 'é impar')
    #positivo ou negativo
    if calculo < 0:
        print(calculo, 'é Negativo')
    else:
        print(calculo, 'é Positivo')
    #inteiro ou decimal
    if calculo == round(calculo):
        print(int(calculo), 'é Inteiro')
    else:
        print(calculo, 'é Decimal')
    
    

    exit()