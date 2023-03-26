num = float(input('Informe o valor do produto: R$'))
form_pag = int(input('''Informe o forma de pagamento: 
[ 1 ] À vista: desconto de 10%
[ 2 ] À vista no cartão: desconto de 5%
[ 3 ] Em até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros:\n'''))
if form_pag == 1:
    print('À vista o valor do produto sai por: R${:.2f}'.format(num*0.9))
elif form_pag == 2:
    print('À vista no cartão o valor do produto sai por R${:.2f}'.format(num*0.95))
elif form_pag == 3:
    print('Em até 2x no cartão o valor do produto sai por: R${:.2f}\nCom a parcela de R${:.2f}'.format(num, num/2))
elif form_pag == 4:
    num_parcelas = int(input('Informe o numero de parcelas: '))
    num = num*1.20
    print('Em 3x ou mais no cartão o valor do produto sai por: R${:.2f}\nCom cada parcela de R${:.2f}'.format(num, num/num_parcelas))