numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))
if numero1 > numero2 > numero3:
    print(numero1, numero2, numero3)

elif numero3 > numero2 > numero1:
    print(numero3, numero2, numero1)

elif numero2 > numero3 > numero1:
    print(numero2, numero3, numero1)

elif numero1 > numero3 > numero2:
    print(numero1, numero3, numero2)

elif numero3 > numero1 > numero2:
    print(numero3, numero1, numero2)

elif numero2 > numero1 > numero3:
    print(numero2, numero1, numero3)