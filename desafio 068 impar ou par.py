import random
print('PAR OU IMPAR')
vitorias = 0
decisao = ''
while True:
    print('-='*40)
    computador = random.randint(0,10)
    jogador = int(input('Digite um valor: '))
    soma = computador + jogador
    Par_Impar = str(input('Par ou Impar: [P/I]: ')).strip().upper()[0]
    while Par_Impar not in 'PI':
        Par_Impar = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'Voce escolher {jogador} e o pc escolheu {computador}, a soma foi {soma}')
    if soma %2 == 0 and Par_Impar == 'P':
        decisao = 'Par'
        print(f'{decisao} Você venceu!!!')
        vitorias += 1
    elif soma %2 != 0 and Par_Impar == 'I':
        decisao = 'Impar'
        print(f'{decisao} Você venceu!!!')
        vitorias += 1
    else:
        break

print(f'{decisao} Você perdeu ')
print(f'o jogador teve um total de {vitorias} vitorias ')
