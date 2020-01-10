lado1 = int(input('Digite o valor do lado "A" de um triangulo: '))
lado2 = int(input('Digite o valor do lado "B" de um triangulo: '))
lado3 = int(input('Digite o valor do lado "C" de um triangulo: '))
#verificar se é um triangulo.
if lado1 == 0 or lado2 == 0 or lado3 == 0:
    print('Não é um triangulo')
#qual tipo de triangulo.
elif lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
    print('Triângulo Equilátero')
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print('Triangulo Isósceles')

elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print('Triangulo Escaleno')
