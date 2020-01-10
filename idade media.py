jovem = int(0)
adulta = int(0)
idosa = int(0)
idadem = int(0)
a = 0
for x in range(10):
    idade = int(input('Infrme sua idade: '))
    idadem = (idade + idadem)
    a += 1
    if idade > 0 and idade < 25:
        jovem += 1

    elif idade > 26 and idade < 60:
        adulta += 1
    
    elif idade > 60:
        idosa += 1
print('De {0} pessoas que entrevistamos {1}% é jovem {2}% é adultas e {3}% é idosas'.format(a, (jovem / a) * 100, (adulta / a) * 100, (idosa / a) * 100))

print('Com base em {0} idades concluimos que a idade media é {1}'.format(a, (idadem /a)))
exit()    