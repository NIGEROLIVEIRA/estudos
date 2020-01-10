zero_vinte_cinco, vinte_seis_cinquenta, cinco_um_sete_cinco, sete_seis_cem = [], [], [], []
def imprimir():
    print('\nDe 0 a 25 tem {} numeros'.format(len(zero_vinte_cinco)))
    print('De 26 a 50 tem {} numeros'.format(len(vinte_seis_cinquenta)))
    print('De 51 a 75 tem {} numeros'.format(len(cinco_um_sete_cinco)))
    print('De 76 a 100 tem {} numeros'.format(len(sete_seis_cem)))

while True:
    print('Digite um numero inteiro para continuar! ou "0" para sair')
    nun = int(input(''))
    if nun == 0 or nun < 0:
        imprimir()
        exit()
    elif nun > 0 and nun <= 25:
        zero_vinte_cinco.append(nun)

    elif nun > 26 and nun <= 50:
        vinte_seis_cinquenta.append(nun)

    elif nun > 51 and nun <= 75:
        cinco_um_sete_cinco.append(nun)
    
    elif nun > 76 and nun <= 100:
        sete_seis_cem.append(nun)


        