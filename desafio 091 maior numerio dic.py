from operator import itemgetter
from random import randint
from time import sleep

jogadores = dict()
for c in range(1, 5):
    jogadores[f'jogador {c}'] = randint(1, 6)
for k,v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('{:=^40}'.format('RANKING'))
ranking = dict
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
p = 1
for k, v in ranking:
    print(f'{p}⁰ lugar : {k} com {v}')
    p += 1