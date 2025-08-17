lista = []
resp = ''
while resp != 'N':
    numeros = int(input('Digite um numero: '))
    lista.append(numeros)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Não entendi, Quer continuar? ')).strip().upper()[0]
print('-=' * 40)
print(f'foram digitados {len(lista)} valores')
lista.reverse()
print(f'lista de forma decrescente {lista}')
if 5 in lista:
    print('o valor 5 esta na lista')
else:
    print('O valor 5 não foi encontrado na lista')