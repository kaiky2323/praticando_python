from time import sleep

def maior_valor(*num):
    maior = list()
    quant = len(num)
    print('-='*20)
    print('Analisando valores...')
    for i, k in enumerate(num):
        print(k, end=' ')
        sleep(0.5)
    print(f'foram informados {quant} numeros')

    if quant <= 0:
        maior = quant

    maior = 0
    for pos, e in enumerate(num):
        if maior < num[pos]:
            maior = e
    print(f'Sendo {maior} o maior valor')


maior_valor(4, 3, 3)
maior_valor(2, 4, 5, 4, 3)
maior_valor(3, 7)
maior_valor()