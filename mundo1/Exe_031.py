distan = float(input('Informe a distância da viagem em Km/h: '))
if distan <= 200:
    valor_pagar = distan*0.5
else:
    valor_pagar = distan*0.45
print('O valor da sua viagem é de R${:.2f}'.format(valor_pagar))
