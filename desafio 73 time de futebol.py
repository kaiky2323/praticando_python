tabela = ('Palmeiras', 'Flamengo', 'Bragantino', 'Cruzeiro', 'fluminense', 'Ceara', 'Atletico', 'Bahia', 'Botafogo', 'Corinthians', 'Fortaleza', 'Mirassol',
           'internacional', 'EC vitoria', 'Gremio', 'São Paulo', 'Vasco da gama', 'juventude', 'Santos ', 'Sport Recife')
print('{:=^50}'.format('\033[32m TABELA CAMPEONATO \033[m'))
print(f'Os primeiros 5 colocados são {tabela[0:5]}')
print('='*50)
print(f'Os ultimos 4 colocados são {tabela[-4:]}')
print('='*50)
print(f'Flamengo esta na posição {tabela.index("Flamengo")+1} ')