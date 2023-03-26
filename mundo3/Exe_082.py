lista = []
lista_pares = []
lista_impares = []
while True:
    lista.append(int(input('Informe um valor: ')))
    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = input('Dejesa continuar ?[S/N]: ').strip().strip()[0]
    if pergunta in 'Nn':
        break
for c in lista:
    if lista[c] % 2 == 0:
        lista_pares.append(lista[c])
    else:
        lista_impares.append(lista[c])
print(f'A lista completa: {lista}\nA lista apenas com numeros pares: {lista_pares}\nA lista apenas com numeros impares: {lista_impares}')