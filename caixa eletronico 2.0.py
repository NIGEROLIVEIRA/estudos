import sys
saque = int(input('Qual valor você deseja sacar: '))
#valor saque nao permitido.
if saque > 600 or saque < 10:
    print('Limite maximo 600 e minimo 10')
    sys.exit()
#contar cedulas ex: saque =556
cem = int(saque / 100) #acha a quantidade de vez que é divizivel por 100= 5.5  usa o int para arredondar para 5
saque = saque % 100 #cria uma var local para armazenar o resto da divisao de 556.Que é 5 de 100 e sobra 56

cinquenta = int(saque / 50) #acha a quantidade de vez que é divizivel por 50= 1.12  usa o int para arredondar para 1
saque = saque % 50 #cria uma var local para armazenar o resto da divisao de 56.Que é 1 de 50 e sobra 6

dez = int(saque / 10) # como 6 nao divide por 10 entao pula para o proximo
saque = saque % 10

cinco =  int(saque / 5)#acha a quantidade de vez que é divizivel por 5=1.2  usa o int para arredondar para 1
saque = saque % 5 #cria uma var local para armazenar o resto da divisao de 6.Que é 1 de 5 e sobra 1

um = saque # Um armazena o que sobra da var saque anterior

print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  1,00 = ',um)