matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma =  maior =0
for l in range (0, 3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um numero para a posição {[l, c]}:'))
       #soma dos pares
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        #descobrir maior numero
        if maior < matriz[1][c]:
            maior = matriz[1][c]

print('+='*40)
#mostra a matriz completa
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
#mostra a soma da 3a coluna
for l in range (0,3):
    for c in range(2,3):
        soma += matriz[l][c]

        print()

print('+='*40)
print(f'soma dos numeros pares: {par}')
print(f'A soma da terceira coluna: {soma}')
print(f'O maior numero da 2a linha é: {maior}')