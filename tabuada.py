a = int(input('Informe o numero da tabuada que deseja ver: '))
tab = 0
print('Tabuada do ', a)
while tab < 10:
    tab += 1
    print(a, 'x', tab, '=', (a * tab))
exit(0)