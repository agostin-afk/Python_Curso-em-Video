listanum = []
c = 0
while True:
    n = int(input('Informe um valor: '))
    if n not in listanum:
        listanum.append(n)
    else:
        print('Valor repetitivo, não será adicionado')
    pergunta = input('Deseja continuar? [S/N]: ')[0].upper().strip()
    if pergunta in 'Nn':
        break
print(f'Os valores da lista foram: {listanum}')
