import random
n1 = input('Informe o nome do priemiro aluno: ')
n2 = input('Informe o nome do segundo aluno: ')
n3 = input('Informe o nome do terceiro aluno: ')
n4 = input('Informe o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
escolha = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolha))
