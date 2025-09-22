from time import sleep

c = ('\033[m', # 0sem cor
    '\033[41m', # 1 vermelho
     '\033[43m', # 2 amarelo
     '\033[44m', # 3 azul
     '\033[46m', # 4 azul claro
     )


def ajuda(com):
    titulo(f'acessando o manual do comando \'{com}\'', 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO', 1)