n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2 )/2
if media >= 6:
    print("""O aluno que tirou {} na primeira prova e {} na segunda tem a media {}
    Esse aluno esta \033[32mAPROVADO!!!""".format(n1, n2, media))
elif media < 6 and media >= 4:
    print("""O aluno que tirou {} na primeira prova e {} na segunda tem a media {}
    Esse aluno esta em \033[33mRECUPERAÇÃO!!!""".format(n1, n2, media))
else:
    print("""o aluno que tirou {} na primeira prova e {} na segunda tem a media {}
    Esse aluno esta \033[31mREPROVADO!!!""".format(n1, n2, media))