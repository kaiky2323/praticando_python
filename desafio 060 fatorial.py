from math import factorial

n = int(input('Digite um numero para calcular o fatorial dele: '))
print('{}! = '.format(n),end=' ')
fat = factorial(n)
while n > 1:
    print(' {} '.format(n), end=' ')
    print('x' if n > 1 else '=', end=' ')
    n -= 1
print(end=' = {}'.format(fat))
