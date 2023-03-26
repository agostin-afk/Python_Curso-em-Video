num1 = float(input('informe o primeiro numero: '))
num2 = float(input('informe o segundo numero: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''Escolha uma opção:
    [1] para somar
    [2] para multiplicar
    [3] para mostar o maior
    [4] para novos numeros 
    [5] para sair do programa
    Sua opção: '''))
    if escolha == 1:
        print('A soma de {} e {} é {}'.format(num1, num2, num1+num2))
    elif escolha == 2:
        print('A multiplicação de {} e {} é igual a {}'.format(num1, num2, num1*num2))
    elif escolha == 3:
        maior = num1
        if maior < num2:
            maior = num2
        print('O maior valor é {}'.format(maior))
    elif escolha == 4:
        num1 = float(input('Informe o novo valor do primeiro numero: '))
        num2 = float(input('Informe o novo valor do segundo numero: '))
print('Fim do programa :D')
