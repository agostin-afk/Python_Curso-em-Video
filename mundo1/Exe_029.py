x = float(input('Informe a velocidade do carro em Km/h: '))
if x > 80:
    valor_pagar = (x-80)*7
    print('Voce passou do limite, sua multa é de R${:.2f}'.format(valor_pagar))
else:
    print('Voce andou dentro das leis de transito :D')
