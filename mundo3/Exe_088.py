import random
import time
lista = []
jogos = []
quantidade = int(input('Quantos jogos você que sortear ?: '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'Jogo numero {i+1}: {l}')
    time.sleep(0.5)
