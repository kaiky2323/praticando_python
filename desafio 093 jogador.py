jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome: '))
partidas = int(input('Partidas jogadas: '))
for g in range (0 , partidas):
    gols.append(int(input(f'Gols na partida {g + 1}: ')))
    jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-='*40)
print(jogador)
print('-='*40)

for k, v in jogador.items():

    print(f'{k}: {v}')

print('-='*40)

print(f'O jogador {jogador['nome']} jogou {partidas} partidas')

for k, v in enumerate(jogador['gols']):
    print(f'Na partida {k + 1} ele fez {v} gol(s).')
print(f'Foi um total de {jogador['total']} gols')