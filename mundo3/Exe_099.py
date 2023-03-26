import time
def maior(* num):
    cont = m = 0
    print('-='*30)
    print('Analizando os valores...')
    for v in num:
        print(f'{v} ', end='')
        time.sleep(0.4)
        if cont == 0:
            m = v
        else:
            if v > m:
                m = v
        cont += 1
    print(f'\nO maior numero foi {m} e foram {cont} numeros contados')


maior(1, 2, 3, 4, 5, 6, 10, 9, 1)
