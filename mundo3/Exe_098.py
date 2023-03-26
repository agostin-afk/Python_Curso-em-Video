import time
def contador(i, f, p):
    for c in range(0, 3):
        if c == 0:
            i = 1
            f = 10
            p = 1
        elif c == 1:
            i = 10
            f = 2
            p = 2
        else:
            i = int(input('Inicio: '))
            f = int(input('Final: '))
            p = int(input('Passo: '))
        if p < 0:
            p *= -1
        if p == 0:
            p = 1
        print('-='*30)
        print(f'Contagem de {i} até {f} de {p} em {p}')
        if i < f:
            cont = i
            while cont <= f:
                print(f'{cont} ', end='')
                time.sleep(0.2)
                cont += p
            print('Fim')
        else:
            cont = i
            while cont >= f:
                print(f'{cont} ', end='')
                time.sleep(0.2)
                cont -= p
            print('Fim')
        print('-='*30)


contador(1, 1, 1)
