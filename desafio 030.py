numero = int(input('Me diga um numero: '))
if numero % 2 == 0:
    print('O numero \033[36m{}\033[m é par'.format(numero))
else:
    print('O numero \033[36m{}\033[m é impar'.format(numero))