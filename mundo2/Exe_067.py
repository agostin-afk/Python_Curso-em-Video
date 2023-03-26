while True:
    num = int(input('Insira um numero para a sua tabuada: '))
    if num < 0:
        print('Numeros negativos não são aceitos!!')
        break
    print('-='*20)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-='*20)
print('Fim do programa')
