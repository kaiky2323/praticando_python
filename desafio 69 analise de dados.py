#criar um programa que leia idade e sexo
#deve perguntar se o usuario quer continuar ou não
#mostrar quantas pessoas tem +18
#quanto homens foram cadastrados
#quantas mulheres tem menos de 20 anos
mulher_menor = Dmaior = homem = 0
while True:
    print('_'*40)
    print('CADASTRO DE PESSOAS')
    print('_'*40)
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo? [F/M]: ')).strip().upper()[0]
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if idade > 18:
        Dmaior += 1
    if sexo == 'F' and idade <= 20 :
        mulher_menor += 1
    if sexo == 'M':
        homem += 1
    if resp == 'N':
        break
print(f'O total de pessoas maiores de 18 foi {Dmaior}')
print(f'{mulher_menor} mulheres com menos de 20 anos.')
print(f'foi cadastrado {homem} homens')