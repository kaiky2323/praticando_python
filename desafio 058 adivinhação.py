import random

print('{:=^40}'.format('ADIVINHAÇÃO'))

jogador = int(input('Digite um numero de 0 a 10: '))
palpite = 1
pc = random.randint(0, 10)
while jogador != pc:
    palpite += 1
    if pc < jogador:
        print('menos')
    else:
        print('mais')
    jogador = int(input('Qual o seu palpite: '))
print('acertou eu realmente pensei no {}. Foram necessario {} palpites'.format(pc, palpite))