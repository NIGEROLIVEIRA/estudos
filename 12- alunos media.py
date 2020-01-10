dic = {11:1.58, 15:1.90, 13:1.80, 14:1.89}

lista = [1.58, 1.60, 1.80, 1.89]

def somar():
    soma = round(0)
    for l in lista:
        soma += l / 4
    return soma

def verificar():
    vr = 0
    for x in dic.keys():
        if x >= 13 and dic.get(x) > s:
            vr += 1
    return vr


s = somar()
v = verificar()
print('Apenas {} alunos esta acima do altura media com mais de 13 anos'.format(v))