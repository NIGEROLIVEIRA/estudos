temperatura_list = {35:'janeiro', 38:'fevereiro', 36:'marco', 32:'abril', 31:'maio',
 37:'junho', 29:'julho', 25:'agosto', 24:'setembro', 26:'outubro', 42:'novembro', 40:'dezembro'}

lista_temp = [35, 38, 36, 32, 31, 37, 29, 25, 24, 26, 42, 40]

soma = round(0, 2)
for t in lista_temp:
    soma += t / 12

print('A temperatura ultrapassou a media anual nos meses de ', end='')
for x in temperatura_list.keys():
    if x > soma:
        print(temperatura_list.get(x), end=', ')