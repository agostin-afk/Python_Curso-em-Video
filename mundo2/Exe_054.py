import datetime

ano_atual = datetime.date.today().year
maior_idade = menor_idade = 0
for i in range(0, 7):
    ano_pessoa = int(input('informe o ano que a {}ª pessoa nasceu: '.format(i + 1)))
    if ano_atual - ano_pessoa < 21:
        menor_idade += 1
    else:
        maior_idade += 1
print('Temos {} pessoas maiores de 18 anos\nE {} pessoas com menos de 18 anos'.format(maior_idade, menor_idade))
