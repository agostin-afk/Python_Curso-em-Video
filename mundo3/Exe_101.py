import datetime


def voto(ano_nasc):
    ano_atual = datetime.datetime.today().year
    idade = ano_atual - ano_nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


nasc = int(input('Informe o ano que você nasceu: '))
print(voto(nasc))
