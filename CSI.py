print('Responda as perguntas com "sim" ou "não"')
a = input('Telefonou para a vítima? ')
b = input('Esteve no local do crime? ')
c = input('Mora perto da vítima? ')
d = input('Devia para a vítima? ')
e = input('Já trabalhou com a vítima? ')
r = [] #var do tipo lista.
while True:
    
    while a == 'sim':   #verifica a resposta.
        a = 1           #acrecenta 1 no valor da var "a" para que no proximo loop a nao seja == 'sim'.
        r.append (1)    #adiciona um valor na var "r"
    while b == 'sim':
        b = 1
        r.append (2)
    while c == 'sim':
        c = 1
        r.append (3)
    while d == 'sim':
        d = 1
        r.append (4)
    while e == 'sim':
        e = 1
        r.append (5)

    len(r) #faz a leitura de quantos caracteres foram salvos na var "r", com base na quantidade ele da a sentença.
    if (len(r)) == 2:
        print('Você é Suspeita!')
    elif  (len(r)) == 3 or (len(r)) == 4:
        print('Você é Cúmplice!')
    elif  (len(r)) == 5:
        print('Você é Assassino!')
    else:
        print('Você é inocente!')
    
    exit()
