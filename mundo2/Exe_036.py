valor_casa = float(input('Informe o valor da casa para o empestimo: '))
salario = float(input('Informe o seu  salario atual: '))
temp_emprest = int(input('Informe em quantos anos pretende parar o emprestimo: '))
prestacao = valor_casa/(temp_emprest*12)
print('Para pagar uma casa de R${:.2f} em {} anos o valor da pretação é de R${:.2f}'.format(valor_casa, temp_emprest, prestacao))
if prestacao > salario*0.3:
    print('Seu emprestimo foi: Negado!!!')
else:
    print('Seu emprestimo foi: Aprovado!!!')
