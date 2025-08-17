temp = []
principal = []
menor = maior = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? '))[0]
    if  resp in 'Nn':
        break
print('-='*30)
print(f'Os dados foram {principal}')
print(f'A quantidade de pessoas cadastradas foram: {len(principal)}')
print(f'Maior peso foi {maior}Kg de', end=' ')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'Menor peso foi {menor}Kg de', end=' ')
for p in principal:
   if p[1] == menor:
        print(f'{p[0]}', end=' ')
