import random
pc_escolha = random.randint(1, 10)
'''print('Seu computador pensou em um numero de 1 a 10, tente advinhar!!')
escolha = int(input('Seu palpite: '))
tentativas = 0
while escolha != pc_escolha:
    if escolha < pc_escolha:
        print('Você errou, tente um numero maior.')
    elif escolha > pc_escolha:
        print('Você errou, tente um numero menor.')
    escolha = int(input('Seu palpite: '))
    tentativas += 1
print('Você acertou, o numero foi {}!!! seu numero de tentativas foram {}'.format(pc_escolha, tentativas))
'''
tentativa = 0
acertou = False
while not acertou:
    jogador = int(input('Qual os seu palpite: '))
    tentativa += 1
    if jogador < pc_escolha:
        print('Você errou, tente um numero maior.')
    elif jogador > pc_escolha:
        print('Você errou, tente um numero menor.')
    else:
        acertou = True
print('Você acertou, o numero foi {}\nSuas tentativas: {}'.format(pc_escolha, tentativa))
