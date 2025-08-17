from random import randint
from time import sleep
listas = list()
jogos = []
tot = 1
print('{:=^20}'.format('MEGA SENA'))
qua_jogos = int(input('Quantos jogos quer que eu sorteie? '))

while tot <= qua_jogos:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in listas:
            listas.append(num)
            cont += 1
        if cont >= 6:
            break
    listas.sort()
    jogos.append(listas[:])
    listas.clear()
    tot += 1
print('-=' *5, f'SORTEANDO {qua_jogos} JOGOS', '-=' *5)
for i, j in enumerate(jogos):
    print(f'JOGO {i+1}: {j}')
    sleep(1)
