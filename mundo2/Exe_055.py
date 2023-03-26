maior = menor = 0
for i in range(0, 5):
    peso = int(input('informe o peso da {}ª pessoa: '.format(i+1)))
    if i == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso no sistema foi {}\nO maior peso do sistema foi {}'.format(menor, maior))
