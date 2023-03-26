l1 = float(input('Informe o primeiro lado do tringulo: '))
l2 = float(input('Informe o segundo lado do tringulo: '))
l3 = float(input('Informe o terceiro lado do tringulo: '))
if l1 < (l2+l3) and l2 < (l1+l3) and l3 < (l2+l1):
    print('Esses segmentos formam um tringulo :D')
else:
    print('Esses segmentos não formam um tringulo :(')
