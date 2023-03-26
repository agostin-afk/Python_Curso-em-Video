numeros = [[], []]
for c in range(1, 8):
    v = int(input(f'Informe o {c}° numero: '))
    if v % 2 == 0:
        numeros[0].append(v)
    else:
        numeros[1].append(v)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros pares são: {numeros[0]}\nOs numeros impares são: {numeros[1]}')
