media_idade = qtd_m20 = 0
homem_velho = ''
maior_idade = 0
for i in range(0, 5):
    print('______{}ª Pessoa______'.format(i+1))
    nome = input('Nome: ').upper().strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').upper().strip()
    if sexo == 'M':
        if maior_idade < idade:
            maior_idade = idade
            homem_velho = nome
    if sexo == 'F':
        if idade < 20:
            qtd_m20 += 1
    media_idade += idade
media_idade /= 5
print('''A media de idade do grupo é: {:.2f}
O homem mais velho tem {} anos e o seu nome é {}
Ao todo são {} mulheres com menos de 20 anos'''.format(media_idade, maior_idade, homem_velho, qtd_m20))
