base = int(input('Digite a base da potencia: '))
expoente = int(input('Digite o expoente: '))
loop = 1
base1 = base 
print(base ** expoente)
while loop < expoente:
    loop +=1
    base = base * base1
print('A Potencia de', expoente, 'sobre ', base1, 'é :', base)

exit(0)