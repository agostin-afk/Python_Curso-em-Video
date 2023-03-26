lista = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'Américo-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')
cinco_primeiros = lista[0:4]
ultimos = lista[-4:]
ordem = sorted(lista)
posicao_fortaleza = lista.index('Fortaleza') + 1
print(f'A lista do brasileirão é:\n{lista}\n{"-="*50}\nOs 5 primeiros times são:\n{cinco_primeiros}\n{"-="*50}\nOs ultimos 5 times são:\n{ultimos}\n{"-="*50}\nA lista em ordem alfabetica fica:\n{ordem}\n{"-="*50}\nA posição que o Fortaleza está é: {posicao_fortaleza}')
