import datetime
import time

cadastro = {'Nome': input('Nome: '), 'Ano de nascimento': int(input('Ano de nascimento: ')),
            'CTPS': int(input('Numero da sua CTPS (0 se não possuir): '))}
cadastro['Idade'] = datetime.datetime.today().year - cadastro['Ano de nascimento']
if cadastro['CTPS'] == 0:
    cadastro['CTPS'] = 'Não possui'
else:
    cadastro['Ano de contratação'] = int(input('Informe o ano de contratação: '))
    cadastro['Salario'] = float(input('Seu salario: '))
    cadastro['Idade para aposentadoria'] = cadastro['Idade'] + (
                (cadastro['Ano de contratação'] + 35) - datetime.datetime.today().year)
print(f'{"DADOS":=^40}')
for k, v in cadastro.items():
    print(f'{k}: {v}')
    time.sleep(0.2)
