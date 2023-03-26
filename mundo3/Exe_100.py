import random
from time import sleep


def sortear(lista):
    for i in range(0, 5):
        lista.append(random.randint(0, 10))
    print('Os numeros sorteados foram: ')
    for v in lista:
        print(f'{v} ', end='')
        sleep(0.5)


def somar_pares(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'\nA soma dos pares deu: {soma}')


numeros = []
sortear(numeros)
somar_pares(numeros)
