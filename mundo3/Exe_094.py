dados = []
pessoas = {}
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = input('Nome: ')
    while True:
        pessoas['Sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('Erro!!\nApenas digite M ou F.')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    dados.append(pessoas.copy())
    while True:
        pergunta = input('Deseja continuar ?[S/N]: ').strip().upper()[0]
        if pergunta in 'SN':
            break
        print('Erro!!\nApenas digite S ou N.')
    if pergunta in 'Nn':
        break
print('-='*30, end='-\n')
print(dados)
print('-='*30, end='-\n')
print(f'    Ao todo temos {len(dados)} pessoas cadastradas')
media = soma/len(dados)
print(f'    A media das idades é de: {media:.2f} anos')
print('    As mulheres cadatradas foram: ')
for p in dados:
    if p['Sexo'] in 'Ff':
        print(f'        -{p["Nome"]}')
print('Pessoas acima da media de idade: ')
for p in dados:
    if p['Idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'    {k} => {v};', end=' ')
        print()
