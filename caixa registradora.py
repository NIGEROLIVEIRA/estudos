cont = 1
for x in range(0, cont + 1):
    print('Qual produto voçê quer?')
    produto = input('| Pastel-1 | salgado-2 | Salada de fruta-3 | Doçe-4 | Refree-5 |:')
    valor = input('Qual o valor: ')
    if float(produto)  <= 0 or float(valor) <= 0:
        exit()
    else:
        print(float(produto) * float(valor))
exit()