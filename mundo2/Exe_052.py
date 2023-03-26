num = int(input('Digite um numero: '))
cont = 0
for i in range(1, num+1):
    if num % i == 0:
        cont += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\033[m')
if cont > 2:
    print('Esse numero não é primo')
else:
    print('Esse numero é primo')
