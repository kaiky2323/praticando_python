valores = [[], []]  # valores[0] = pares, valores[1] = ímpares

for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        valores[0].append(n)  # adiciona na lista de pares
    else:
        valores[1].append(n)  # adiciona na lista de ímpares
valores[0].sort()
valores[1].sort()
print(f'Todos os números pares: {valores[0]}')
print(f'Todos os números ímpares: {valores[1]}')
