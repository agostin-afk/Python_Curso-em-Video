import random
import time
import operator

jogo = {'Jogador 1': random.randint(1, 6),
        'Jogador 2': random.randint(1, 6),
        'Jogador 3': random.randint(1, 6),
        'Jogador 4': random.randint(1, 6)}
rank = []
print('Placar: ')
for k, v in jogo.items():
    print(f'{k} -> {v} pontos')
    time.sleep(0.5)
rank = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print(f'{"RANKING":-^30}')
for i, v in enumerate(rank):
    print(f"{i + 1}° lugar: {v[0]} com {v[1]} pontos")
