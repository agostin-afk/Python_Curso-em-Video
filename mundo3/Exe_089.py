lista = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    lista.append([nome, [nota1, nota2], media])
    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = input('Deseja continuar ?[S/N]: ').strip().upper()[0]
    if pergunta in 'Nn':
        break
print('-'*30)
print(f'{"Nº.:":<4}{"Nome:":<10}{"Media:":>8}')
print('-'*30)
for v, i in enumerate(lista):
    print(f'{v+1:<4}{i[0]:<10}{i[2]:>8.2f}')
while True:
    print('-'*30)
    opc = int(input('Deseja saber as notas de qual aluno?(999 para parar): '))
    if opc == 999:
        break
    if opc <= len(lista):
        print(f'Notas do aluno {lista[opc-1][0]}: {lista[opc-1][1]}')

