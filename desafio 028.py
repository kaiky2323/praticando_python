import random
from time import sleep

print('-=-' *20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
numeropc = random.randint(0,5)
numeroEu = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(3)
if numeroEu == numeropc:
    print('Você ganhou, eu realmente pensei no {}! '.format(numeropc))
else:
    print('Ganhei, eu pensei no {} e não no {}'.format(numeropc,numeroEu))