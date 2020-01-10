numero = float(input('Entre com um numero para verificar se é inteiro ou decimal: '))

if numero == round(numero):# numero inteiro arredonda por ele mesmo
    print(int(numero), 'é numero Inteiro')
elif numero != round(numero):#numero decimal nao arredonda por ele mesmo
    print(numero, 'é numero decimal')
