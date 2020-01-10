
def resposta_certa():
    loop = 0
    for y in dic_resposta:
        if dic_resposta.get(y) == dic_prova.get(y):
            loop += 1
    return loop


def perguntas():#executa a pergunta 10 vezes.
    resposta_aluno = {}
    for x in range(1, perguntas_gabarito + 1):
        letra = input('Informe a resposta da questao {}: '.format(x)) #faz o input das respostas
        resposta_aluno [x] = letra #anexa as resposta na lista resposta.
    return resposta_aluno


def imprimir():
    print('A maior nota foi {0} A menor nota foi {1}'.format(maior, menor))
    print('Total de alunos que foram analizados : {}'.format(alunoq))
    print('A media das notas é {0}'.format(round(media / alunoq, 2)))

############################################### INICIO DO PROGRAMA ##############################################
perguntas_gabarito = int(input('Digite a quantidade de questoes voce quer anexar no "gabarito": ')) #resposta certa
dic_prova, media, pontos_aluno, alunoq, maior, menor = {}, 0, 0, 0, 0, 0
for b in range(1, perguntas_gabarito + 1):
    nun = int(input('Digite o numero da pergunta: '))
    letra = input('Digite a letra da resposta: ')
    dic_prova [nun] = letra #dicionario resposta certa



while True:   #loop para cadastrar mais alunos
    media += pontos_aluno                         
    aluno = input('Deseja verificar um aluno: S/N: ')
                               

    if aluno != 's': #verifica aresposta de "aluno = input('Deseja verificar um aluno: S/N: ')"
        imprimir()                      
        exit()
        
    else:
        alunoq += 1  #Total de Alunos que utilizaram o sistema;
        nome = input('Digite o Nome do aluno: ')
        
        dic_resposta = perguntas()      #Recebe as respostas das perguntas e passa pro dicionario de "respostas"
        pontos_aluno = resposta_certa()  #chama a funçao resposta_certa e recebe a pontuaçao do aluno
       
        #encontra a nota maior e a menor
        if alunoq == 1:
            maior = menor = pontos_aluno
        else:
            if pontos_aluno > maior:
                maior = pontos_aluno                
            elif pontos_aluno < menor:
                menor = pontos_aluno


                



        






        

        
            