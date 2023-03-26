nomes = ('pedro', 'curso', 'amor', 'sono', 'come', 'oculos', 'vidro', 'peixe', 'batata', 'carro', 'moto', 'dinheiro', 'poder', 'musica')
for c in nomes:
    print(f'\nO nome {c} possui as vogais: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
