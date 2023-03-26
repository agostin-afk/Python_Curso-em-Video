sexo = input('informe o seu sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Sexo invalido\nTente novamente[M/F]:').strip().upper()[0]
print('Sexo {} registrado com sucesso!!!'.format(sexo))
