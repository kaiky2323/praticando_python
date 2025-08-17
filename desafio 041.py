import datetime
nascimento = int(input('Qual o seu ano de nascimento? '))
ano = datetime.date.today().year
atual = ano - nascimento
print('Quem nasceu em {} tem {} anos'.format(nascimento, atual))

if atual <= 9:
    print('classificação: MIRIM')
elif atual >= 10 and atual <= 14:
    print('Classificação: INFANTIL')
elif atual >= 15 and atual <= 19:
    print('classificação: JÚNIOR')
elif atual >= 20 and atual <= 25:
    print('classificação: SÉNIOR')
else:
    print('classificação: MASTER')