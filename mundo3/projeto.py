def arquiviExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!!')


def Lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS:')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(aqv, nome='<desconhecido>', idade=0):
    try:
        a = open(aqv, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!!')
        else:
            print(f'Novo resgistro de {nome} adicionado')
            a.close()


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro. Digite apenas numeros inteiros.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuario.')
            return None
        else:
            return n


def cabecalho(msg, t=30):
    linha(t)
    print(f'{msg}'.center(t))
    linha(t)


def linha(t=30):
    print('-'*t)


def sistema(menu):
    global num
    cabecalho('Registro de Pessoas')
    i = 0
    for c in menu:
        i += 1
        print(f' {i} - {c}')
    linha()
    n = leiaInt('Sua escolha: ')
    return n
