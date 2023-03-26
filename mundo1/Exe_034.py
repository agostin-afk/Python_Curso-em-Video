salario = float(input('Informe o seu salario: '))
if salario > 1250:
    salario = salario*1.1
else:
    salario = salario * 1.15
print('Seu novo salario é de R${:.2f}'.format(salario))
