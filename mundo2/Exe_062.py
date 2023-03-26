termo = int(input('informe o priemiro termo: '))
razao = int(input('informe a razão: '))
numero_termos = 10
total_termos = 0
flag_while = 1
while numero_termos != 0:
    total_termos += numero_termos
    while flag_while <= total_termos:
        print('{} -> '.format(termo), end='')
        termo += razao
        flag_while += 1
    print('Pausa')
    numero_termos = int(input('Quantos termos a mais você que ver ?: '))
print('Programa finalizado')
