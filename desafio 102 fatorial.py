def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} = ', end='')
    return f


print(fatorial(5, show=True))

help(fatorial)