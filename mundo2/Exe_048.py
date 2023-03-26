soma = 0
cont = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print('A soma dos {} numeros deu: {}'.format(cont, soma))
#for i in range(0, 501):
#    if i % 2 != 0 and i % 3 == 0:
#        soma += i
#        cont += 1
#print('A soma dos {} numeros deu: {}'.format(cont, soma))
