l1 = float(input('Informe o primeiro lado do triangulo: '))
l2 = float(input('Informe o segundo lado do trinagulo: '))
l3 = float(input('Informe o terceiro lado do trinagulo: '))
if l1 < (l2+l3) and l2 < (l3+l1) and l3 < (l1+l2):
    print('Os valores formam um trinagulo')
    if l1 == l2 == l3:
        print('O trinagulo formado é EQUILÁTERO')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('O triangulo formado é ISÓCELES')
    else:
        print('O trinagulo formado é ESCALENO')
else:
    print('Os valores não formam um triangulo')
