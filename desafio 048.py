#faça um programa que calcule a soma entre todos os números que
# são múltiplos de três e que se encontram
s = 0
cont = 0

for c in range(1, 501, 2):
    if c %3 == 0:
        cont += 1
        s += c
print('A soma dos {} valores solicitados é {}'.format(cont, s))
