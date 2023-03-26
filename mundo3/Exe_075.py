lista = (int(input('informe um numero: ')), int(input('informe mais um numero: ')), int(input('informe o penultimo numero: ')), int(input('informe o ultimo numero: ')))
print(f'Seus numeros foram {lista}\nNa lista teve um total de {lista.count(9)} numeros 9')
if 3 in lista:
    print(f'O numero 3 apareceu na posição: {lista.index(3)+1}')
print('Os numeros pares foram: ')
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        print(lista[c], end=' ')
