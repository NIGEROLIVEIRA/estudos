numero = int(input('Digite um numero inteiro para verificar se é impar ou par: '))
divisor = numero % 2
if divisor == 0:
    print(numero, 'é Par')
else:
    print(numero, 'é Imparar')
