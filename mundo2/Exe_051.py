print('''
=============================
    10 termos de uma P.A
=============================
''')
primeiro_termo = int(input('informe o primeiro termo da P.A: '))
razao = int(input('informe a razão da P.A: '))
decimo = primeiro_termo + 10*razao
for i in range(primeiro_termo, decimo, razao):
    print(i, end=' -> ')
print('Acabou')