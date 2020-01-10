ano = int(input('Digite um ano para verificar '))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print(ano ,' É ano Bissexto')
else:
    print(ano ,' Não é ano Bissexto')