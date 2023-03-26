soma = 0
for i in range(0, 6):
    num = int(input('informe o {}° numero: '.format(i+1)))
    if num % 2 == 0:
        soma += num
print('A soma dos numeros pares deu: ', soma)
