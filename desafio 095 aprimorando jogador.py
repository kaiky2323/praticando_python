from time import sleep

dados = list()
while True:
    jogador = dict()
    gols = list()
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input('Partidas jogadas: '))
    gols.clear()
    for g in range (0 , partidas):
        gols.append(int(input(f'Gols na partida {g + 1}: ')))
        jogador['gols'] = gols
    jogador['total'] = sum(gols)
    dados.append(jogador.copy())
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Responda apenas com Sim(S) ou Não(N): ')).strip().upper()[0]
    if opc in 'N':
        break

print('-='*40)
print(f'\033[0;32m{"cod":<4} {"NOME":<10} {"GOLS":<10} {"TOTAL":>20}\033[m')
for c, j in enumerate(dados):
    print(f'\033[0;32m{c:<4}\033[m {j['nome']:<10} {str(j['gols']):<10} {j['total']:>20}')
print('-='*40)
while True:
    esc = int(input('Qual jogador deseja consultar? (999 parar):'))
    if esc == 999:
        break
    while esc < 0 or esc >= len(dados):
        esc = int(input('Jogador inexistente: '))
    if esc <= len(dados) -1:
        print('{:=^40}'.format(f'CONSULTA JOGADOR {dados[esc]['nome']}').title())
        for k, v in enumerate(jogador['gols']):
            print(f'Na partida {k} ele fez {v} gol(s)')
print('Finalizando...')
sleep(2)
print('FINALIZADO')