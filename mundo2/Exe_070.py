soma = prod_mais_barato = maiores = cont = 0
prod_menor = ' '
print('''------------------------------
        Loja do gostin      
------------------------------''')
while True:
    print('_'*30)
    nome = input('Informe o nome do produto: ')
    preco = float(input('informe o preço do produto: R$'))
    pergunta = ' '
    cont += 1
    if cont >= 1:
        prod_mais_barato = preco
        prod_menor = nome
    else:
        if prod_mais_barato > preco:
            prod_menor = nome
            prod_mais_barato = preco
    if preco > 1000:
        maiores += 1
    soma += preco
    while pergunta not in 'SsNn':
        pergunta = input('Deseja continaur [S/N] ?: ').strip().upper()[0]
    if pergunta in 'Nn':
        break
print(f'''A compra deu um total de R${soma:.2f}
O produto mais barato foi {prod_menor} com o valor de R${prod_mais_barato:.2f}
teve um total de {maiores} produtos com o valor maior de R$1000.00''')
