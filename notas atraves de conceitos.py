nota1 = float(input('Digite a primeira Nota: '))
nota2 = float(input('Digite a segunda Nota: '))
media = (nota1 + nota2) / 2
print('Primeira nota:', nota1)
print('Segunda nota:', nota2)
print('Media:', media)
#notas por conceito.
if media >=9 and media <=10:
    print('Parabens você foi aprovado---------Conseito "A"')
elif media >=7.5 and media < 9:
    print('Parabens você foi aprovado---------Conseito "B"')
elif media >= 6 and media < 7.5:
    print('Parabens você foi aprovado---------Conseito "C"')
elif media >= 4 and media < 6:
    print('Infelismente você foi reprovado----Conseito "D"')
elif media >= 0 and media < 4:
    print('Infelismente você foi reprovado----Conseito "E"')