resp = ''
numero= maior = menor = soma = digitos = media  = 0
inicio = 1
while resp != 'n':
    numero = float(input('Digite um numero: '))
    digitos += 1
    soma += numero
    media = soma/digitos
    if inicio == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    inicio += 1
    resp = str(input('quer continuar: ').strip().lower())
print('A media dos valores digitados é {}'.format(media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))