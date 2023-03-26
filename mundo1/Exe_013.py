salario = float(input('Informe o seu salario para o calculo do aumento de 15%:\nR$'))
aumento = ((100+15)/100)
salario_novo = salario*aumento
print('O seu novo salario com o aumento de 15% é: R${:.2f}'.format(salario_novo))
