num_homens = num_mulheres_menores = maiores = 0
while True:
    print('-'*30)
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = input('informe o sexo ?[M/F]: ').upper().strip()[0]
    if idade >= 18:
        maiores += 1
    if idade < 20 and sexo == 'F':
        num_mulheres_menores += 1
    if sexo == 'M':
        num_homens += 1
    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = input('Deseja continuar ? [S/N]: ').upper().strip()[0]
    if pergunta == 'N':
        break
print(f'''Programa finalizado!
O total de homens cadastrados foi de: {num_homens}
O total de mulheres com menos de 20 anos cadastradas foi de: {num_mulheres_menores}
O total de pessoas com mais de 18 anos foi de {maiores}''')
