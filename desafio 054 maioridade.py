import datetime

pessoas = int(input('Quantas pessoas: '))
menor = 0
maior = 0
for c in range(1, pessoas+ 1):
    nascimento = int(input('Qual o ano de nascimento da {} pessoa: '.format(c)))
    idade = datetime.date.today().year - nascimento

    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('A quantidade de pessoas maiores de idade é {}'.format(maior))
print('A quantidade de pessoas menor de idade é {}'.format(menor))