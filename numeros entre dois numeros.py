numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
for i in range(numero_1, numero_2):
    print('o intervalo entre {0} e {1} : é: {2}'.format(numero_1, numero_2, i))
print('A soma dos numeros é: ', numero_1 + numero_2)
exit(0)