import datetime
ano = int(input('Insira um ano para verificar, caso queira no ano atual digite 0: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
