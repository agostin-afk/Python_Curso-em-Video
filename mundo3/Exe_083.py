lista = []
x = input('Sua equação: ')
for c in x:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) != 0:
    print('Sua expressão é invalida!')
else:
    print('Sua expressão é válida!')

