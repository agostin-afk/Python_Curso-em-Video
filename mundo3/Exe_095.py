jogador = {}
partidas = []
grupo = []
while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador: ')
    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou ?:'))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'  -Quantos gols {jogador["Nome"]} fez na pardida {c+1}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    grupo.append(jogador.copy())
    while True:
        pergunta = input('Deseja continuar ?[S/N]: ').strip().upper()[0]
        if pergunta in 'SN':
            break
    if pergunta == 'N':
        break
print('-='*30, end='-\n')
print('cod. ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(grupo):
    print(f'{k+1:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30, end='-\n')
while True:
    busca = int(input('Mostrar dados de qual jogador ?(999 para finalizar): '))-1
    if busca == 999:
        break
    if busca > len(grupo):
        print(f'Erro!!\nNão existe jogador com o codigo {busca}')
    else:
        nome = grupo[busca]['Nome']
        print(f'{f"DADOS DO JOGADOR {nome}":-^30}')
        for i, g in enumerate(grupo[busca]['Gols']):
            print(f'    No jogo {i+1}, fez {g} gols')
print('-='*30, end='-\n')
