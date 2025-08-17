print('{:=^40}'.format('FIBONACCI'))
termos = int(input('Quantos termos deseja mostrar? '))
n1 = 0
n2= 1
print('~'*40)
print('{} -> {}'.format(n1, n2),end='-> ')
cont = 3
while cont <= termos:
    n3 = n1 + n2
    print('{} -> '.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1
print('fim')