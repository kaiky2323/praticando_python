n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))

print("Os tres valores formam um triango", end=' ')
if n1 == n2 and n2 == n3:
    print('Equilatero')
elif n1 != n2 != n3 != n1:
    print('Escaleno')
else:
    print('Isoceles')
