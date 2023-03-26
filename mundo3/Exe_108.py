import moduloExe_108

p = int(input('informe o valor: R$'))
print(f'''O dobro de R${moduloExe_108.moeda(p)} é : R${moduloExe_108.moeda(moduloExe_108.dobro(p))}
A metade de R${moduloExe_108.moeda(p)} é: R${moduloExe_108.moeda(moduloExe_108.metade(p))}
Aumentando em 10% temos: R${moduloExe_108.moeda(moduloExe_108.aumentar(p, 10))}''')
