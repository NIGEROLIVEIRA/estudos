inp, loop, lista = 0, 0, 0
while loop < 5:
    loop += 1
    inp = int(input('Digite um numero: '))
    lista += inp
print('A soma dos numeros é:', lista)
print('A media dos numeros é:', lista / loop)
exit(0)
