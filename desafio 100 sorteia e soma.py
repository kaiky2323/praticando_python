from random import randint
from time import sleep

lista = list()
lista_par = list()
def sorteia(*num):
    print('Sorteando 5 numeros...', end='')
    for c in range(5):
        numero_random = randint(0, 10)
        print(numero_random, end=' ')
        sleep(0.5)
        lista.append(numero_random)

def soma_par():
    soma = 0
    for i, k in enumerate(lista):
        if lista[i] %2 == 0:
            soma += k
            lista_par.append(k)

    print(f'os numero pares da lista {lista} é {lista_par} e soma dela é igual a {soma}')

sorteia()
print()
soma_par()
