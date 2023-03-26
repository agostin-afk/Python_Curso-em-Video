num = int(input('informe um numero para calcular o seu fatorial: '))
c = num
fat = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat = fat*c
    c -= 1
print(fat)
