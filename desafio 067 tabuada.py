print('{:=^40}'.format('TABUADA'))

while True:
    n = int(input('Você quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} X {cont}= {n * cont}')
        cont += 1
print('Programa encerrado, volte sempre!')