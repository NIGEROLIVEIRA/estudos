import sys
valora = int(input('Digite o valor de "A": '))
if valora == 0:
    sys.exit(0)
valorb = int(input('Digite o valor de "B": '))
valorc = int(input('Digite o valor de "C": '))
# formula de bakara.
delta = valorb ** 2 - 4 * valora * valorc
#condicionais a equação não possui raizes reais
if delta < 0:
    print('A equação não possui raizes reais')

#condicional  a equação possui apenas uma raiz real
elif delta == 0:
    x1 = (- valorb / (2 * valora))
    x2 = ( valorb / (2 * valora))
    print('A equação possui apenas uma raiz real X1:', x1,' e X2:', x2)
#Condicional a equação possui duas raiz reais
elif delta > 0:
    x1 = ((- valorb + (delta ** (1/2))) / (2 * valora))
    x2 = ((- valorb - (delta ** (1/2))) ** 1/2) / 2
    x3 = ((2 * valora) ** 1/2) / 2
    print('A equação possui duas raiz reais X1:',x1 ,' e X2:', x2, '/', x3)

print(delta)