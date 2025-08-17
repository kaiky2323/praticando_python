print('{:=^40}'.format('TABELA DE PRECOS'))
tabela = ('mochila', '120,00',
          'Lapis', '1,75',
          'Borracha', '2,00',
          'Estojo', '15,35',
          'caderno', '25,80')
for pos in range(0, len(tabela)):
    if pos %2 ==0:
        print(f'{tabela[pos]:.<30}', end=' ')
    else:
        print(f'R${tabela[pos]}')