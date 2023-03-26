import moduloExe_107

p = int(input('informe o valor: R$'))
print(f'''O dobro de R${p} é : R${moduloExe_107.dobro(p)}
A metade de R${p} é: R${moduloExe_107.metade(p)}
Aumentando em 10% temos: R${moduloExe_107.aumentar(p, 10)}''')
