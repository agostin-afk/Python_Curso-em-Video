import random
numeros = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
print('Os valores sorteados foram: ', end='')
for c in range(len(numeros)):
    print(numeros[c], end=' ')
print(f'\nO maior valor da lista foi {max(numeros)}\nO menor valor da lista foi {min(numeros)}')
