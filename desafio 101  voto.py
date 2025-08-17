import datetime
from time import time

def voto(nasci):
    voto_obg = datetime.date.today().year - nasci
    if voto_obg < 16:
        return f'Com {voto_obg}: Não pode votar'
    elif voto_obg >= 16 and voto_obg < 18 or voto_obg >= 65:
        return f'Com {voto_obg}: Voto opcional'
    elif voto_obg >= 18:
        return f'Com {voto_obg}: Voto obrigatorio'




ano_nasci = int(input('Qual ano você nasceu: '))
decisao= voto(ano_nasci)
print(f'{decisao}')