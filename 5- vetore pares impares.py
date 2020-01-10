def entrada():
    lista = []
    inicial = int(input('Digite o numero inicial: '))
    final = int(input('Digite o numero final: '))
    for x in range(inicial, final + 1):
        lista.append(x)
    return lista

def separar_par():
    par = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
    return par

def separar_impar():
    impar = []
    for i in lista:
        if i % 2 != 0:
            impar.append(i)
    return impar

lista = entrada()
par = separar_par()
impar = separar_impar()

print('Todos {0}'.format(lista))
print('Par {0}'.format(par))
print('Impar {0}'.format(impar))