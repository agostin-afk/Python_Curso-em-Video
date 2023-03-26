#centralizar
x = input('qual o seu nome ? ')
print('olá {:20}, como vai ?'.format(x))#{: numero de caracteres}
print('olá {:>20}, como vai ?'.format(x))#{: 20 caracteres alinhados na direita}
print('olá {:<20}, como vai ?'.format(x))#{: 20 caracteres alinhados para a esquerda}
print('olá {:^20}, como vai ?'.format(x))#{: 20 caracteres centralizados} variavel x fica no centro
print('olá {:=^20}, como vai ?'.format(x))#{: caracteres para preencher'=' 20 vezes centralizado}
