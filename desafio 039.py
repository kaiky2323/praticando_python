ano = int(input('Ano de nascimento: '))
#criando variavel
idade = 2025 - ano

#Criando escolhas
print('Quem nasceu em {} tem {} anos em 2025'.format(ano, idade))
if idade == 18:
    print('\033[33mVoce deve se alistar\033[m \033[1;33m IMEDIATAMENTE!!')

elif idade >= 19:
    alistamento = idade - 18
    anoAlista = 2025 - alistamento
    print('Você deveria ter se alistado ha {} ano(s)'.format(alistamento))
    print('Seu alistamento foi em {}'.format(anoAlista))

elif idade <= 17:
    alistamento = 18 - idade
    anoAlista = 2025 + alistamento
    print('Ainda faltam {} ano(s) para o alistamento'.format(alistamento))
    print('Seu alistamento será em {}'.format(anoAlista))