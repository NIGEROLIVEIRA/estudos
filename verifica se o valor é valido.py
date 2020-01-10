numero = float(input('Informe um numero entre "0" e "10":' ))
while True:
    while numero < 1 or numero > 10:
        print(numero,'Não é um Valor invalido!')
        numero = float(input('Informe um numero entre "0" e "10":' ))
    while numero >= 1 and numero <= 10:
        print(numero,'É um valor valido!')
        numero = 0
    exit(0)