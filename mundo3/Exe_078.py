lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Informe o valor da posição {c+1}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Os valores digitados foram: {lista}')
print(f'O maior numero foi {maior}\nNas posições:')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...', end='')
print(f'\nO menor valor foi {menor}\nNas posições:')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...', end='')
