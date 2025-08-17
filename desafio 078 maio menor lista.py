numero = []
for cont in range (0, 5):
    numero.append([int(input(f'Digite um numero para a posição {cont}: '))])
print(f'Você digitou os valores {numero}')
print(f'O maior valor é o {max(numero)} nas posições ',end='')
for i, v in enumerate(numero):
    if v == max(numero):
        print(f'{i}...')
print(f'O menor valor digitado foi {min(numero)} nas posições ',end='')
for i, v in enumerate(numero):
    if v == min(numero):
        print(f'{i}...')
