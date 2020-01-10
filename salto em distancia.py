def entra_dados(): #entrada dos valores
    salto_lista = []                 #armazena em lista os valores dos saltos
    for s in range(1, 6):            #faz input dos valores dos saltos
        salto = float(input('{0}° salto quantos metros: '.format(s)))
        salto_lista.append(salto)
    return salto_lista

def deleta_lista():# deleta o maior e o menor salto para media de 3 saltos
    lista_media.sort()
    lista_media.pop(0)
    lista_media.pop(3)

def media_tres():# media de 3 saltos
    media = 0
    for l in lista_media:
        media += l
    return media

def media_todos():# media de todos os cinco saltos
    media_all = 0
    for m in lista:
        media_all += m
    return media_all

def ordenar_lista():# ordena a lista Da list "lista_ordenada"
    lista_ordenada.sort()

def imprimir(): #imprime os a tabela de resultado
    print('\nAtleta: {0}\n'.format(nome))
    print('Primeiro Salto: {0} m'.format(lista_imprime[0]))
    print('Segundo Salto: {0} m'.format(lista_imprime[1]))
    print('Terceiro Salto: {0} m'.format(lista_imprime[2]))
    print('Quarto Salto: {0} m'.format(lista_imprime[3]))
    print('Quinto Salto: {0} m\n'.format(lista_imprime[4]))
    print('Melhor salto: {0} m'.format(lista_ordenada[4]))
    print('Pior salto: {0} m'.format(lista_ordenada[0]))
    print('Média dos demais saltos: {0} m\n'.format(round(media_all / 5, 2)))
    print('Resultado final:')
    print('{0}: {1} m'.format(nome, round(media / 3, 2)))
    
nome = input('Nome do atleta: ') #entar com o nome do atleta
lista = entra_dados()           #chama e recebe dados da funcao entra_dados
lista_imprime = lista[:]            # faz uma copia da "lista" original para imprimir sem alteraçao na ordem
lista_media = lista[:]              #faz copia de "lista" original para apagar o maior e o menor
lista_ordenada = lista[:]        #faz copia da "lista" original e ordena para obter o maior e o menor dos 5 saltos
ordenar_lista()                 #chama a funcao que ordena a lista "lista_ordenada"
deleta_lista()                  #chama a funcao que deleta maior e menor da lista "lista_media"
media = media_tres()            
media_all = media_todos()
imprimir()                  


    