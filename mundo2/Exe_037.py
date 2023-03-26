num = int(input('Insira um numero para converção de base: '))
escolha = int(input('''Escolha uma das opçoes:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL
Sua escolha: '''))
if escolha == 1:
    print('{} em Binário é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} em Octal é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} em Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente')
