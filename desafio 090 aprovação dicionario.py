from time import sleep

aluno = dict()

print('{:=^40}'.format('MEDIA ALUNO'))
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Media de {aluno['nome']}:  '))
#Se a nota for menor que 7 o aluno esta reprovado
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'
print('='*40)
for k, v in aluno.items():
    sleep(2)
    print(f'{k}: {v}')