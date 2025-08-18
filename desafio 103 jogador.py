'''Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos
gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''
import math
def ficha(nome, gol):
    if nome.strip()== '':
        nome = 'Desconhecido'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    return f'O jogador {nome} fez {gol} gol(s)'

print(ficha(nome=str(input('Nome do jogador: ')), gol=input('gol(s): ')))
