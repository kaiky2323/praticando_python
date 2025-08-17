import random

n1 = ('Pedra')
n2 = ('papel')
n3 = ('tesoura')

lista = [n1, n2, n3]
computador = random.choice(lista)

print('''[ 1 ] Pedra
[ 2 ] Papel 
[ 3 ] Tesoura ''')
jogador = int(input('Qual a sua jogada? '))

if computador == n1 and jogador == 2:
    print('Você venceu, eu escolhi {}'.format(computador))
elif jogador == 1 and computador == n2:
    print('você perdeu, eu escolhi {}'.format(computador))
elif computador == n2 and jogador == 3:
    print('você venceu, eu escolhi {}'.format(computador))
elif jogador == 2 and computador == n3:
    print('Você perdeu, eu escolhi {}'.format(computador))
elif jogador == 3 and computador == n1:
    print('Você perdeu, eu escolhi {}'.format(computador))
elif jogador == 1 and computador == n3:
    print('Você venceu, eu escolhi {}'.format(computador))
else:
    print('empatamos')
if jogador >= 4:
    print('jogada invalida')