primeiro_termo = int(input('Informe o primeiro termo da P.A: '))
razao = int(input('Informe a razão da P.A: '))
c = 10
termo_n = primeiro_termo
while c > 0:
    c -= 1
    print('{}'.format(termo_n), end='')
    print(' -> ' if c > 0 else '', end='')
    termo_n += razao
