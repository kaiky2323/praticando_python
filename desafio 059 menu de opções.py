from time import sleep

opcao = 0
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
while opcao != 5:
    print('{:=^40}'.format('Opção'))
    print('''Qual ação deseja realizar
    [ 1 ] Somar 
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('Digite a opção: '))

    if opcao == 1:
        print('a soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('O resultado da multiplicação de {} X {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        print('O maior numero entre {} e {} é {}'.format(n1, n2, max(n1, n2)))
    elif opcao == 4:
        print('Digite novos numeros')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
if opcao == 5:
    print('Saindo do programa...')
sleep(3)