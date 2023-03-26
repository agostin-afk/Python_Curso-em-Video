def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('Erro. Digite apenas numeros inteiros.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuario.')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num_float = float(input(msg))
        except (ValueError, TypeError):
            print('Erro. Digite apenas numeros reais.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuario.')
            return 0
        else:
            return num_float


num_int = leiaInt('Digite um valor inteiro: ')
print(f'O numero que voce digitou foi {num_int}')
num_float = leiaFloat('Digite um numero real: ')
print(f'O numero que voce digitou foi {num_float}')