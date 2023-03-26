import random
win = 0
while True:
    escolha_pc = random.randint(1, 10)
    escolha_numero_jogador = int(input('informe o seu numero: '))
    escolha_jogador = ' '
    while escolha_jogador not in 'PpIi':
        escolha_jogador = input('qual a sua escolha ?[P/I]: ').strip().upper()[0]
    numero = escolha_pc + escolha_numero_jogador
    if escolha_jogador == 'P':
        if numero % 2 == 0:
            print(f'voce ganhou!! \nO numero foi {numero}, deu Par e voce ganhou.')
            win += 1
        else:
            break
    elif escolha_jogador == 'I':
        if numero % 2 != 0:
            print(f'voce ganhou!!\nO numero foi {numero}, deu Impar e voce ganhou.')
            win += 1
        else:
            break
print(f'voce perdeu, pois o numero foi {numero} :(\nSeu total de vitorias foi de: {win}')