
quant = float(input('Quantas temperaturas deseja testar: '))
maior, menor, loop, total, quante = 0, 0, 0, 0, quant
while quant > 0:
    loop += 1
    quant -= 1
    temp = float(input('Informe a temperatura: '))
    total += temp
    if loop == 1:
        maior, menor = temp, temp
    else:
        if temp > maior:
            maior = temp
        elif temp < menor:
            menor = temp

print('A maior temperatura foi {0} a menor foi {1} e a temperatura media foi {2}'.format(maior, menor, round(total / quante, 2)))
exit()