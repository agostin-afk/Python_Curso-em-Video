preco = float(input('informe o valor do produto para obter o desconto de 5%:\nR$'))
desconto = ((100-5)/100)
novo_preco = preco * desconto
print('O novo valor do produto é:\nR${:.2f}'. format(novo_preco))
