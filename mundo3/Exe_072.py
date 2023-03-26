numeros = (
'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    pergunta = int(input('Informe umnumero de 0 a 20: '))
    if pergunta in range(0, 21):
        break
print(numeros[pergunta])
