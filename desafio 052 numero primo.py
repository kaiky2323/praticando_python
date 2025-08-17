numero = int(input('Digite um numero inteiro: '))
divisao = 0
for c in range(1, numero + 1):
    if numero %c ==0:
        print('\033[33m', c, '\033[m', end=' ' )
        divisao += +1
    else:
        print('\033[31m', c,'\033[m', end=' ')

print('''
O numero {} foi divisivel {} vezes 
por isso ele'''.format(numero, divisao))
if divisao > 2:
    print('NÃO É PRIMO')
else:
    print('É PRIMO')
