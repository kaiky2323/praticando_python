from datetime import datetime

dados = dict()
print('{:=^40}'.format('INSS'))
dados['nome'] = str(input('Nome: '))
dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - dados['nascimento']
dados['carteira'] = int(input('Carteira (0 não tem): '))
if dados['carteira'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salario: '))
    if dados['sexo'] in 'M':
        dados['aposentadoria'] = dados['contratação'] - dados['nascimento'] + 35
    if dados['sexo'] in 'F':
        dados['aposentadoria'] = dados['contratação'] - dados['nascimento'] +30
else:
    dados['carteira'] = 'Não tem'
del dados['nascimento']
print('=-' * 40)
for k,v in dados.items():
    print(f'{k}: {v}')