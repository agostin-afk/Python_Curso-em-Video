def aumentar(preco=0, taxa=0, formatacao=False):
    res = preco + (preco*taxa/100)
    return res if not formatacao else moeda(res)


def diminuir(preco=0, taxa=0, formatacao=False):
    res = preco - (preco*taxa/100)
    return res if not formatacao else moeda(res)


def metade(preco=0, formatacao=False):
    res = preco/2
    return res if not formatacao else moeda(res)


def dobro(preco=0, formatacao=False):
    res = preco*2
    return res if not formatacao else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=10, diminuicao=0):
    print('-'*30)
    print('RESUMO DO VALOR:'.center(30))
    print('-'*30)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{diminuicao}% de redução: \t{diminuir(preco, diminuicao, True)}')
