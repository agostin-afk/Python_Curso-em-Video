temp_lista = []
lista = []
maior = menor = 0
while True:
    temp_lista.append(input('Nome: '))
    temp_lista.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = temp_lista[1]
    else:
        if temp_lista[1] > maior:
            maior = temp_lista[1]
        if temp_lista[1] < menor:
            menor = temp_lista[1]
    lista.append(temp_lista[:])
    temp_lista.clear()
    pergunda = ' '
    while pergunda not in 'SsNn':
        pergunda = input('Dejesa continuar ?[S/N]: ').strip().upper()[0]
    if pergunda in 'Nn':
        break
print(f'O maior peso foi kg {maior:.2f}, das pessoas: ', end='')
for c in lista:
    if c[1] == maior:
        print(f'{c[0]} ', end='')
print(f'\nO menor peso foi kg {menor:.2f}, das pessoas: ', end='')
for c in lista:
    if c[1] == menor:
        print(f'{c[0]} ', end='')
print(f'\nForam cadastadas {len(lista)} pessoas')
