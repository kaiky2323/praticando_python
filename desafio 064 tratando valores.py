valor = int(input('Digite um numero [999 para parar]: '))
digitos = 0
soma = 0
while valor != 999:
    soma += valor
    digitos += 1
    valor = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} vezes e a soma dos digitos é {}'.format(digitos, soma))