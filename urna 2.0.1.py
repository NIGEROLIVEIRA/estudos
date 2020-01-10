
def contar_votos():#contar e imprimir votos
    total = 0   #var que armazena todos os votos contados
    for x in range(1, 7):
        print(dic.get(x), 'recebeu', voto.count(x), 'votos')
        total += voto.count(x)
    
    for x in range(5, 7):# imprime a porcentagen de nulos e brancos
        print('Os votos {0} é {1} %'.format(dic.get(x), round(100 - (total - voto.count(x)) / total * 100, 2)))
    
dic = {1:'Joao', 2:'Jose', 3:'Maria', 4:'Pedro', 5:'Nulo', 6:'Branco'}

voto = []    #lista que armazena a quantidade de votos antes de contar

while True:
    print(dic)
    votar = int(input(' '))
    if votar <= 0:      #verificador para sair do programa
        break

    voto.append(votar)  #add votos na lista

contar_votos()
