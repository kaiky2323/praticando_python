
lista = tuple(int(input('Digite um numero: '))for cont in range (0,4))
print(f'Os numeros digitados foram {lista}')
if 9 in lista:
    print(f'O numero "9" foi digitado {lista.count(9)} vezes')
else:
    print('O numero "9" não foi digitado')
if 3 in lista:
    print(f'O numero " 3 " esta na posição {lista.index(3)+1}')
else:
    print('o numero "3" não foi digitado')
print('Os valores pares digitados foi : ',end=' ')
for n in lista:
    if n %2 == 0:
        print(n, end=' ')