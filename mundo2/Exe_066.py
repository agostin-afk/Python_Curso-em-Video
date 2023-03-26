soma = 0
while True:
    x = int(input('insira um numerp (digite 999 para parar): '))
    if x == 999:
        break
    soma += x
print(f"A soma dos valores digitados deu: {soma}")
