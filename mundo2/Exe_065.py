pergunta = ''
cont = 0
soma = 0
maior = menor = 0
while pergunta != 'N':
    x = int(input('Informe um numero: '))
    soma += x
    cont += 1
    if cont == 1:
        maior = menor = x
    else:
        if maior < x:
            maior = x
        if menor > x:
            menor = x
    pergunta = input('Deseja continuar ? [S/N]:\n').upper().strip()[0]
media = soma/cont
print('A media dos valores deu: {}\nO maior e menor valor foram, respectivamente: {} e {}'.format(media, maior, menor))
