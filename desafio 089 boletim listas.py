from time import sleep

boletim = list()
print('{:=^40}'.format('BOLETIM'))
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Primeira nota do aluno: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) /2
    boletim.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:=^40}'.format('NOTAS FINAIS'))
print(f'{"No":<4} {"NOME":<10} {"NOTA":>4}')
print('=-'*40)
for i, a in enumerate (boletim):
    print(f'{i:<4} {a[0]:<10} {a[2]:10.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(2)
        break
#consulta do aluno
    if opc <= len(boletim) -1:
        print(f'As notas de {boletim[opc][0]} Foram {boletim[opc][1]}')

