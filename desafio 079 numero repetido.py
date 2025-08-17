lista = []
numero = 0
resp = 0
while resp != 'N':
    numero = int(input('Digite o numero que deseja: '))
    if numero in lista:
        print('ja temos esse numero')
    else:
        lista.append(numero)
        print('Numero adicionado com sucesso')
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
print(sorted(lista))