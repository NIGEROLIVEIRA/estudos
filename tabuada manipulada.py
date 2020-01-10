tabuada = int(input('Informe qual tabuada você deseja ver: '))
ini = int(input('Informe em qual numero deve começar: '))
fin = int(input('Informe em qual numero deve acabar: '))
#verificar as entradas do usuario.
if ini > fin:
    print('Valores incorretos')
    exit()
#fazendo a tabuada.
print('Vou montar a tabuada de {0} começando em {1} e terminando em {2}'.format(tabuada, ini, fin))
for x in range(ini, fin + 1):
    print(tabuada, 'x', x, '=', (tabuada * x))
print('\n')
exit()