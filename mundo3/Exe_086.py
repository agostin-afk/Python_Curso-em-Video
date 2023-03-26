lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for i in range(0, 3):
        lista[c][i] = int(input(f'informe o valor da posição [{c+1}, {i+1}]: '))
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{lista[c][i]:^6}]', end='')
    print()