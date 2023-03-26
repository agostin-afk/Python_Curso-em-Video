def escreva(msg):
    x = len(msg)+4
    print('='*x)
    print(f'  {msg}')
    print('='*x)


mensagem = input('informe a mensagem: ')
escreva(mensagem)
