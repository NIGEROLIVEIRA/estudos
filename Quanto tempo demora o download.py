tamanho = float(input('Qual o tamanho do arquivo em MB: '))
link = float(input('Qual a velocidade do link de internet: '))
kbps = (link * 102.4)
mb = (tamanho * 1024)
tempo = (mb / kbps) / 60
print('Seu download vai demorar aproximadamente', tempo, 'Minutos')