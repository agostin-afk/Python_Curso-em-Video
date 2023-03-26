def leia(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('valor invalido, digite apenas numeros')
        if ok:
            break
    return valor


n = leia('Digite um numero: ')
print(f'Voce acabou de digitar: {n}')
