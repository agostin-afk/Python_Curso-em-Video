produtos = ('Lápis', 0.75, 'Mochila', 185, 'Caderno', 35, 'Borracha', 1.80, 'Caneta', 2, 'Estojo', 10.45, 'Corretivo', 5, 'Sapato', 75)
print('-'*40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-'*40)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f'R$ {produtos[c]:>6.2f}')
print('-'*40)
