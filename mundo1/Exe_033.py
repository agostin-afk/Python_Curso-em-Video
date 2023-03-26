n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))
maior = n1
menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior valor é {}\nO menor valor é {}'.format(maior, menor))
