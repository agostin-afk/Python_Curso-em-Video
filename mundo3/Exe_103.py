def jogador(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s).')


n = input('Nome do jogador: ')
gols = input('Quantidade de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if n.strip() == '':
    jogador(g=gols)
else:
    jogador(n, gols)
