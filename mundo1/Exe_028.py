import random
import time
print('-='*30, '\nJOGO DE ADVINHAR\n', '-='*30)
x = int(input('Infome um numero: '))
print('Processando...')
time.sleep(1.2)
escolha_pc = random.randint(1, 5)
if x == escolha_pc:
    print('Parabens você acertou o numero :D')
else:
    print('Voce errou o numero :( ele foi o {}'.format(escolha_pc))
