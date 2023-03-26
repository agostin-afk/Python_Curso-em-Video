import time
import random
print('-='*20)
print('GAME------JOKENPÔ------GAME')
escolha_jogador = int(input('''Escolha uma das opçoes:
[1] Pedra
[2] Papel
[3] Tesoura
Sua escolha: '''))
escolha_pc = random.randint(1,3)
time.sleep(.5)
print('JO')
time.sleep(.5)
print('KEN')
time.sleep(.5)
print('PÔ')
if escolha_pc == 1:
    if escolha_jogador == 1:
        print('Empate!!!\nAmbos escolheram Pedra')
    elif escolha_jogador == 2:
        print('Parabens, você ganhou pois escolheu papel e o computador escolheu Pedra')
    elif escolha_jogador == 3:
        print('Voce perdeu, pois escolheu Tesoura e o computador escolheu Pedra, tente novamente')
    else:
        print('valor inválido, tente novamente')
elif escolha_pc == 2:
    if escolha_jogador == 1:
        print('Voce perdeu, pois escolheu Pedra e o computador escolheu Papel, tente novamente')
    elif escolha_jogador == 2:
        print('Empate!!!\nAmos escolheram Papel')
    elif escolha_jogador == 3:
        print('Parabens, você ganhou pois escolheu Tesoura e o computador escolheu Pedra')
    else:
        print('valor inválido, tente novamente')
else:
    if escolha_jogador == 1:
        print('Parabens, você ganhou, pois escolheu Pedra e o computador escolheu Tesoura')
    elif escolha_jogador == 2:
        print('Voce perdeu, pois escolheu Papel e o computador escolheu Tesoura, tente novamente')
    elif escolha_jogador == 3:
        print('Empate!!!\nAmbos escolheram Tesoura')
    else:
        print('valor inválido, tente novamente')
