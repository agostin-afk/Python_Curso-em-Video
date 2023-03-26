from projeto import *
from time import sleep
aqv = 'cadastros.txt'
if not arquiviExiste(aqv):
    CriarArquivo(aqv)
while True:
    resposta = sistema(['Ver pessoas cadastradas', 'Cadastrar pessoa', 'Sair do sistema'])
    if resposta == 1:
        Lerarquivo(aqv)
        sleep(0.75)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome =  input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(aqv, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema...')
        sleep(0.5)
        break
    elif resposta is None:
        break
    else:
        print('Erro! Digite uma opção válida!')
        sleep(0.75)
