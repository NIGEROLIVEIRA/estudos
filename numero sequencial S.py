nun1, nun2 = 1, 1
nsoma1, nsoma2, sequencia = 0, 0, ''
for x in range(1, 11):
    if x == 1:
        sequencia += str(nun1) + '/' + str(nun2)
    else:
        sequencia +=  ' + ' + str(nun1) + '/' + str(nun2)
    nsoma1 = nun1 + nsoma1
    nsoma2 = nun2 + nsoma2
    nun1 += 1
    nun2 += 2
print('S = ', sequencia, '=', nsoma1, nsoma2) 