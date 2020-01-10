print('Bem vindo a hamburgueria.')

def calculo_preco():                                     #funcao encontra o preco  e multiplica pela quantidade.
        if codigo in dicpreco.keys():
            preco = dicpreco.get(codigo)
            codi [codigo] = quantidade * preco

dicpreco = {100 : 1.20, 101 : 1.30, 102 : 1.50, 103 : 1.20, 104 : 1.30, 105 : 1}
dicitens = {100:'cachorro quente', 101:'bauru simples', 102:'bauru com ovos', 103:'hamburguer', 104:'cheseeburguer', 105:'refrigerante'}
codi = {}
while True:
    print(dicitens)
    resp = input('Adicionar produto S/N: ')
    if resp != 's':
        break

    codigo = int(input('Digite o codigo do produto: '))
    quantidade = int(input('Digite a quantidade: '))

    calculo_preco()                                     # chama a funcao para calcular e armazenar dados no dicionario "codi"
    
    




def busca_valores(codi):# funcao busca values nos dicionarios
    conta = 0
    for x in codi:                                                #passa os valores de codi para x.
        if x in dicitens.keys():                                  #verifica se x esta entre as chaves de "dicitens".
            print(dicitens.get(x), '----', round(codi.get(x), 2)) #imprime o value referente a chave que esta em "x"
            conta += float(codi.get(x))                           #converte os valores para float e soma na variavel conta.
    print('Valor total--', round(conta, 2))                       #imprime o valor total que esta em variavel conta

busca_valores(codi)