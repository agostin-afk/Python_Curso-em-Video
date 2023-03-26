def fatorial(num, show=False):
    i = num
    for c in range(1, num):
        num *= c
    if show:
        while i >= 1:
            print(f'{i} {"x" if i >1 else "="} ', end='')
            i -= 1
    print(num)


def fatorial_2(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c} {"x" if c > 1 else "="} ', end='')
    print(f)


fatorial(5, show=True)
fatorial_2(5, show=True)