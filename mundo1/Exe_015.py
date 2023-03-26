km = float(input('Informe am distancia percorrida com o carro, em Km:\n'))
dias = int(input('Infome o tempo que o carro foi alugado, em dias:\n'))
valor = (dias*60)+0.15*km
print('O valor do aluguel para pagar é: R${:.2f}'.format(valor))
