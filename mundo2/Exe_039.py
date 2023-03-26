import datetime
ano = int(input('Informe o ano que você nasceu: '))
if datetime.date.today().year - ano == 18:
    print('Parabens!!!\nAs forças armadas esperam por você :D')
elif datetime.date.today().year - ano < 18:
    print('você aidna não pode servir pois faltam {} anos'.format(18 -(datetime.date.today().year - ano)))
else:
    print('Já passou da hora de você se alistar, vá para um quartel para quitar a sua divida de alistamento')
