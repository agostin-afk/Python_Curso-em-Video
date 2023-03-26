c = int(input('informe ate qual termo da sequencia de fibonacci você quer ver: '))
i = c
t1 = t3 = 0
t2 = 1
while i > 0:
    print('{}'.format(t3), end='')
    print(' -> ' if i > 1 else ' -> Fim do programa', end='')
    t1 = t2
    t2 = t3
    t3 = t1+t2
    i -= 1
