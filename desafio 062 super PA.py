print('{:=^40}'.format('Progressão'))
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
total = 0
mais_termo = 10
termo1 = mais_termo
while mais_termo != 0:
    total = total + mais_termo
    while c < total:
       print('{} -> '.format(termo),end='')
       termo+=   razao
       c += 1
    print('PAUSA')
    mais_termo = int(input('Quantos termos a mais você quer mostrar? '))
    termo1 = termo1 + mais_termo
print('Pogressão finalizada com {} termos mostrados'.format(termo1))