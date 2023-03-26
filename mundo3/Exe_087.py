lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Informe o valor da posição [{l + 1}, {c + 1}]: '))
soma_pares = soma_terceira_coluna = maior_linha_3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^6} ]', end='')
        if lista[l][c] % 2 == 0:
            soma_pares += lista[l][c]
        if l == 1 and c == 0:
            maior_linha_3 = lista[l][c]
        if l == 1:
            if maior_linha_3 < lista[l][c]:
                maior_linha_3 = lista[l][c]
        if c == 2:
            soma_terceira_coluna += lista[l][c]
    print()
print(f'A soma dos numeros pares foi: {soma_pares}\nA soma da terceira coluna foi: {soma_terceira_coluna}\nO maior valor da linha 3 é o numero: {maior_linha_3}')
