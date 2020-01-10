valor = float(input('Quantos você ganha por hora: '))
horas = float(input('Quantas horas você trabalha no mês: '))
salario = valor * horas
liquido = 11+8+5
print('Seu salario bruto é ', salario)
print('Desconto de INSS ',salario - ((8 / 100) * salario))
print('Desconto de Sindicato ',salario - ((5 / 100) * salario))
print('Salario Liquido ',salario - (((11+8+5) / 100) * salario))