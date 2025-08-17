print('{:=^40}'.format('Progressão'))
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
while c < 10:
   print(termo, end=' -> ')
   termo += razao
   c += 1
print('Acabou')