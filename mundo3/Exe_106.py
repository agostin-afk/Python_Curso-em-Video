def ajuda(comand):
    help(comand)


while True:
    com = input('Função ou biblioteca: ')
    if com.upper() == 'FIM':
        break
    else:
        ajuda(com)
print('Volte sempre!!')
