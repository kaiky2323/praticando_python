n = soma = digitos = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    soma += n
    digitos += 1
print(f'Você digitou {digitos} vezes. A soma dos digitos é {soma}')