


lista = [1, 5, 6, 4, 6, 9, 7, 45, 78, 95, 12, 46, 3]
#################################################################
print('Foram armazenados {0} numeros'.format(len(lista)))
for n in lista:
    print(n, end=' ')
#################################################################
lista.reverse()
for i in lista:
    print(i)
#################################################################
print('A soma da lista é', sum(lista))
#################################################################
conta = 0
for c in lista:
    conta += 1
print('A media da lista é', round(sum(lista) / conta, 2))
##################################################################
print('Estes valores estao acima da media ', end='')
for v in lista:
    if v > sum(lista) / conta:
        print(v, end=',')
##################################################################
print('\nEstes valores estao abaixo de 7 : ', end='')
for v in lista:
    if v < 7:
        print(v, end=',')
#################################################################
print('\ngood by')