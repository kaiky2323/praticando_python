def leiaint(num=0):
    ok = False
    valor = 0
    while True:
        numero = str(input(num))
        if numero.isnumeric():
            ok = True
            valor = int(numero)
        else:
            print('\033[31mERRO! digite um numero inteiro valido\033[m')
        if ok:
            break
    return valor


#programa principal
numero = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o valor {numero}')
