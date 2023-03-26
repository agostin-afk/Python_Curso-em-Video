frase = input('informe a frase para analise de palindromo: ').upper().strip()
frase = ''.join(frase.split())
inverso = ''
for i in range(len(frase)-1, -1, -1):
    inverso += frase[i]
print('O inverso de {} é {}'.format(frase, inverso))
if frase == inverso:
    print('É um palindromo!!!')
else:
    print('Não é um palindromo ')
