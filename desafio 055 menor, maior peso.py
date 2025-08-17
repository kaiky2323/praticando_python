leve = 0
pesado = 0

for c in range(1,6):
    peso = float(input('Qual o peso da {} pessoa? '.format(c)))
    if c == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
print('O maior peso lido foi {}'.format(pesado))
print('O menor peso lido foi {}'.format(leve))
