aluno = {'nome': input('Nome: ')}
aluno['media'] = float(input(f'Media do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado!'
elif aluno['media'] >= 5:
    aluno['Situação'] = 'Recuperação!'
else:
    aluno['Situação'] = 'Reprovado!'
for k, v in aluno.items():
    print(f'{k} - {v}')
