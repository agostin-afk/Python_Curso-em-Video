alt = float(input('informe a sua altura: '))
peso = float(input('agora informe o seu peso para o calculo do IMC: '))
imc = peso/(alt**2)
print('Seu IMC é {:.2f} e você está: '.format(imc), end='')
if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('no peso ideal')
elif imc < 30:
    print('com sobrepeso')
elif imc < 40:
    print('com obesidade')
else:
    print('com obesidade mórbida')
