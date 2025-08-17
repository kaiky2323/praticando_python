dados = list()
pessoas = dict()
soma = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
    while pessoas['sexo'] not in 'FM':
        pessoas['sexo'] = str(input("Responda apenas com F ou M: ")).strip().upper()[0]
    pessoas['idade'] = float(input('Idade: '))
    soma += pessoas['idade']
    dados.append(pessoas.copy())
    opc = str(input('Quer continuar?  ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Responda apenas com S ou N: ')).strip().upper()[0]
    if opc in 'N':
        break
print('='*40)
print(f'Ao todo temos {len(dados)} pessoas cadastradas')
media = soma/len(dados)
print(f'A media de idade é {media} anos.')
print(f'As mulheres cadastradas foram', end=' ')
for p in dados:
    if p['sexo'] in 'F':
        print(f'{p['nome']}', end=', ')
print()
print('Lista de pessoas acima da media ')
for p in dados:
    if p['idade'] > media:
        print('      ',end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('===FIM===')
