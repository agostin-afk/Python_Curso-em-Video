lista = []
for c in range(0, 5):
    n = int(input('Informe um valor: '))
    if c == 0 or n >= lista[-1]:
        lista.append(n)
        print('Valor adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos+1}')
                break
            pos += 1
print(f'A lista ordenada fica: {lista}')