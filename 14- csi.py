
def entrada():
    contar = 0
    for x in pergunta:
        p = input('{0}: '.format(x))
        if p == 'sim':
            contar += 1
    return contar
##############################################################
def julgamento():
    opcao = {1:'Inocente', 2:'Suspeito', 3:'Cumplice', 4:'Cumplice', 5:'Culpado'}
    if contar in opcao.keys():
        print('\n', opcao.get(contar))
###############################################################

pergunta = ['\nTelefonou para a vítima?',
            '\nEsteve no local do crime?',
            '\nMora perto da vítima?',
            '\nDevia para a vítima?', 
            '\nJá trabalhou com a vítima']

contar = entrada()
julgamento()
