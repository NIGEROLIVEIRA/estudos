def inicio():
    nome = input('Informe o nome do aluno: ')
    for v in nome:
        for n in ['1234567890-+/*,;.!@#$%¨&*()']:
            if v in n:
                print('\n\n\nNo total {0} alunos teve notas acima ou na media!'.format(final))
                print('Fim da aplicaçao\n\n\n')
                exit()
    return nome
#######################################################################################
def entrada_de_dados():
    lista_notas = []
    for x in range(1, 5):
        notas_entrada = float(input('Digite a {0}° Nota: '.format(x)))
        lista_notas.append(notas_entrada)
    return lista_notas
########################################################################################
def calculo_media():
    media = sum(notas) / 4
    return media
########################################################################################
def media_final():
    final = 0
    if media >= 7:
        final += 1
    return final

fim = 0
while True:
    nome = inicio()
    notas = entrada_de_dados()
    media = calculo_media()
    final = media_final()
    fim += final

