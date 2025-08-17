lista = list()
lista_impar = list()
lista_par = list()
resp = ''
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar [S/N]? '))
    if resp in "nN":
        break
for pos, valor in enumerate(lista):
    if valor %2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
print(f'Os numeros pares são {lista_par}')
print(f'Os numeros impares são {lista_impar}')