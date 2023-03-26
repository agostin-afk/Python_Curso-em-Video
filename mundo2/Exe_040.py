nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1+nota2) / 2
if media >= 7:
    print('Parabens!!!\nVocê foi aprovado com media {:.2f}'.format(media))
elif media >= 5:
    print('Você ficou de Recuperação com media {:.2f}'.format(media))
else:
    print('Você foi reprovado com media {:.2f}'.format(media))
