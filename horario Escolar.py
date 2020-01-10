horario = input('Qual horario você estuda? "M matutino" "V vespentino" "N noturno"')

if horario == 'm':
    print('"Bom dia"')
elif horario == 'v':
    print('"Boa tarde"')
elif horario == 'n':
    print('"Boa noite"')
else:
    print('"Horario nao encontrado"')