jogador = {}
partidas = []
jogador['Nome'] = input('Nome do jogador: ')
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou ?:'))
for c in range(0, total):
    partidas.append(int(input(f'  -Quantos gols {jogador["Nome"]} fez na pardida {c+1}: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-='*30, end='-\n')
print(jogador)
print('-='*30, end='-\n')
for k, v in jogador.items():
    print(f'    -O campo {k} tem o valor {v}')
print('-='*30, end='-\n')
print(f'O  jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'    No {i+1} jogo, o {jogador["Nome"]} fez {v} gols')
print(f'Foi um total de {jogador["Total"]} Gols')
