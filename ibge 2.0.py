a = int(input('Digite a população do pais "A": '))
b = int(input('Digite a população do pais "B": '))
taxa_a = float(input('Digite a taxa de crescimento atual do pais "A": '))
taxa_b = float(input('Digite a taxa de crescimento atual do pais "B": '))
anos = 0
if a < b:
    while a < b:
        a += (taxa_a / 100) * a
        b += (taxa_b / 100) * b
        anos += 1
else:
    while a > b:
        a += (taxa_a / 100) * a
        b += (taxa_b / 100) * b
        anos += 1

print('Levaria ', anos, 'anos para que o pais B alcance ou ultrapasse o pais A')
print('População do pais A', round(a))
print('População do pais B', round(b))
exit(0)