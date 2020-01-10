
def entrada():
    lista = []
    for s in palavra:
        lista.append(s)
    return lista

def verificar():
    consoante = []
    for c in letras: #verifica se as letras de "c" estao em "a" se sim Armazena o valor em "consoante"
        for a in ['bcdfghjklmnpqrstvxz']:
            if c in a:
                consoante.append(c)
    return consoante

palavra = input('Digite uma palavra: ')

letras = entrada()
consoante = verificar()
print('{0} consoantes: {1}'.format(len(consoante), consoante))


