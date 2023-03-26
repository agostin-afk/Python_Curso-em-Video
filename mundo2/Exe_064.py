x = 0
soma = 0
c = 0
while x != 999:
    x = int(input('insira um numero: '))
    if x != 999:
        soma += x
        c += 1
print('A soma dos valores deu: {}\nFoi digitados {} numeros'.format(soma, c))
