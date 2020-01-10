a, b, anos = 80000, 200000, 0
while a < b:
    a += (3 / 100) * a
    b += (1.5 / 100) * b
    anos += 1
else:
    print('Levaria ', anos, 'para que o pais A alcance ou ultrapasse o pais B')
    print('População do pais A', round(a))
    print('População do pais B', round(b))
exit(0)
