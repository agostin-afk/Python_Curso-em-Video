lista = []
while True:
    lista.append(int(input('Informe um valor: ')))
    resp = input('Deseja continuar ?[S/n]: ')[0].upper().strip()
    if resp in 'Nn':
        break
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'A lista em ordem decrecente fica {lista}')
if 5 in lista:
    print('A lista possui o numero 5')
