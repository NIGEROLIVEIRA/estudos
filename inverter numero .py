
def entrada_dados():
    nun = input('Digite um numero inteiro positivo: ')
    return nun

def transforma():
    lista = []
    for n in numero:
        lista.append(n)
    lista.reverse()
    return lista


numero = entrada_dados()
lista = transforma()
print(''.join(lista))