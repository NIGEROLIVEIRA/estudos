nun = int(input('Digite um numero inteiro:'))
div = ''
divisivel = 0
div2 = 0
for x in range(1, nun + 1):
    div2 += 1
    if nun % x == 0:
        div += '-' + str(x)
        divisivel += 1
        
    else:
        pass
if divisivel > 2:
    print('Este numero não é "Primo"')
    print('Ele pode ser dividido por: {0}'.format(div))
    print('Ele foi testado {0} vezes para chegar ao resultado final'.format(div2))
elif divisivel <= 2:
    print('Este numero é "Primo"')

exit()