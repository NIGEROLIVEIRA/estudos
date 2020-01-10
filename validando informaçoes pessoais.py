a = input('Qual seu Nome : ')
b = float(input('Qual sua Idade : '))
c = float(input('Qual seu Salario Liquido : '))
d = input('Qual seu Sexo: "f" Feminino "m" Masculino : ')
e = input('Qual seu Estado Civil: "s" Solteiro(a) "c" Casado(a) : ')
print('#' * 500)
while True:
    if (len(a)) > 3:
        print('Nome:', a, '--Nome validado com sucesso!')
    else:
        print('Nome:', a, '--Não é um Nome valido!')

    if b > 0 and b < 150:
        print('Idade:', b, '--Idade validado com sucesso!')
    else:
        print('Idade:', b, '--Não é uma Idade valida!')

    if c > 0:
        print('Salario:', c, '--Salario validado com sucesso!')
    else:
        print('Salario:', c, '--Não é um Salario valido!')

    if d == 'f' or d == 'm':
        print('Sexo', d, '--Sexo validado com sucesso!')
    else:
        print('Sexo', d, '--Não é um Sexo valido!')

    if e == 's' or e == 'c':
        print('Estado Civil', e, '--Estado Civil validado com sucesso!')
    else:
        print('Estado Civil', e, '--Não é um Estado Civil Valido!')
    exit(0)