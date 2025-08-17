palavras = ('APRENDER', 'JOGAR', 'FOCO', 'DISCIPLINA', 'RIQUEZA',' REALEZA')
vogal = ("AEIOU")
print('{:=^60}'.format('VOGAIS DAS PALAVRAS'))
for pos in palavras:
    print(f'\n na palavra {pos} temos:', end=' ')
    for letra in pos:
        if letra in 'AEIOU':
            print(letra, end=' ')