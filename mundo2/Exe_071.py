print('='*30)
print('{:^30}'.format('Banco do Agostin'))
print('='*30)
valor = int(input('Informe o valor: '))
'''cedula_50 = cedula_20 = cedula_10 = cedula_1 = 0
while True:
    if valor >= 50:
        cedula_50 += 1
        valor -= 50
    elif valor >= 20:
        cedula_20 += 1
        valor -= 20
    elif valor >= 10:
        cedula_10 += 1
        valor -= 10
    elif valor >= 1:
        cedula_1 += 1
        valor -= 1
    else:
        break
print(f'Voce recebera:\n{cedula_50} Notas de R$50.00\n{cedula_20} Notas de R$20.00\n{cedula_10} Notas de R$10.00\n{cedula_1} Notas de R$1.00')
'''
cedula = 50
total_cedula = 0
total = valor
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
