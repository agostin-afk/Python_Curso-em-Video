import datetime
ano_nasc = int(input('Informe o ano que você nasceu: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc
print('O atleta tem {} anos'.format(idade))
if idade < 9:
    clas = 'Mirin'
elif idade < 14:
    clas = 'Infantil'
elif idade < 19:
    clas = 'Junior'
elif idade < 25:
    clas = 'Sênior'
else:
    clas = 'Master'
print('Classificação: {}'.format(clas))
