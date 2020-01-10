def entra_dados(): #entrada dos valores
    salto_lista = []                 #armazena em lista os valores dos saltos
    for s in range(1, 8):            #faz input dos valores dos saltos
        salto = float(input('{0}° nota do jurados: '.format(s)))
        salto_lista.append(salto)
    return salto_lista

def deleta_lista():# deleta o maior e o menor salto para media de 5 saltos
    lista_media.sort()
    lista_media.pop(0)
    lista_media.pop(5)

def media_cinco():# media de 5 saltos
    media = 0
    for l in lista_media:
        media += l
    return media

def ordenar_lista():# ordena a lista Da list "lista_ordenada"
    lista_ordenada.sort()

def imprimir(): #imprime os a tabela de resultado
    print('\nAtleta: {0}\n'.format(nome))
    print('Nota: {0}'.format(lista_imprime[0]))
    print('Nota: {0}'.format(lista_imprime[1]))
    print('Nota: {0}'.format(lista_imprime[2]))
    print('Nota: {0}'.format(lista_imprime[3]))
    print('Nota: {0}'.format(lista_imprime[4]))
    print('Nota: {0}'.format(lista_imprime[5]))
    print('Nota: {0}\n'.format(lista_imprime[6]))
    print('Resultado final:')
    print('Atleta: {0}\n'.format(nome))
    print('Melhor nota: {0}'.format(lista_ordenada[6]))
    print('Pior nota: {0}'.format(lista_ordenada[0]))
    print('Média: {0}\n'.format(round(media / 5, 2)))
    
    print('{0}: {1}'.format(nome, round(media / 5, 2)))
    
nome = input('Nome do atleta: ') #entar com o nome do atleta
lista = entra_dados()           #chama e recebe dados da funcao entra_dados
lista_imprime = lista[:]            # faz uma copia da "lista" original para imprimir sem alteraçao na ordem
lista_media = lista[:]              #faz copia de "lista" original para apagar o maior e o menor
lista_ordenada = lista[:]        #faz copia da "lista" original e ordena para obter o maior e o menor dos 5 saltos
ordenar_lista()                 #chama a funcao que ordena a lista "lista_ordenada"
deleta_lista()                  #chama a funcao que deleta maior e menor da lista "lista_media"
media = media_cinco()            
imprimir()                  


    