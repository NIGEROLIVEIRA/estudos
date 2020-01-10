data = input('Digite uma data no formato dd/mm/aaaa para validar: ')
dia, mes, ano = map(int, data.split('/'))
#verifica mes e ano.
if mes <= 0 or mes > 12 or ano <= 0:
    print(dia, '/', mes, '/', ano,' Nao é uma data valida')
#verifica ultimo dia mes.
if mes in (1, 3, 5, 7, 8, 10, 12):
    ultimodia = 31
#ano bissexto
elif mes == 2:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        ultimodia = 29
    else:
        ultimodia = 28
else:
    ultimodia = 30

#validar dia
if dia <= 0 or dia > ultimodia:
    print(dia, '/', mes, '/', ano,' Nao é uma data valida')
else:
    print(dia, '/', mes, '/', ano,' é uma data valida')