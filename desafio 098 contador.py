from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
#contar na ordem crescente
    print('-='*20)
    if i < f:
        while i < f:
            i += p
            print(i, end=' ')
            sleep(0.5)
        print('Fim!')


#contar na ordem decrescente
    if i > f:
        while i > f:
            print(i, end=' ')
            i -= p
            sleep(0.5)
        print('Fim!')


#criar o proprio contador
    if f < 0:
        p *= -1
        while i > f:
            i -= p
            print(i, end=' ')
            sleep(0.5)


contador(0, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Sua vez de criar um contador.')
contador(i=int(input('Inicio: ')), f=int(input('Fim: ')), p=int(input('Passo: ')))