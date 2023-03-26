import random
n1 = input('informe o nome do primeiro aluno: ')
n2 = input('informe o nome do segundo aluno: ')
n3 = input('informe o nome do terceiro aluno: ')
n4 = input('informe o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresnetação será:\n', lista)
