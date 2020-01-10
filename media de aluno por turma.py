aluno = int(input('Informe a quantidade de alunos: '))
clase = int(input('Informe a quantidade de turmas disponiveis: '))

if (aluno / clase) <= 40:
    print('Foi acomodado em media {0} alunos por turma'.format(aluno / clase))
elif (aluno / clase) > 40:
    print('''Sera necessario contruir mais salas de aula! para acomodar todos os alunos
    falta em media {0} vagas por turma'''.format(int((aluno / clase) - 40)))