def lnota(*notas, situacao = False):

    '''ao declarar que a situação = True
    mostra a situação da turma: Boa, Razoavel, Ruim'''


    resultado = {
        'total' : len(notas),
        'media' : sum(notas)/len(notas),
        'maior' : max(notas),
        'menor' : min(notas)
    }
    if situacao:
        if resultado['media'] > 7:
            resultado['situacao'] = 'Boa'
        elif resultado['media'] >= 5:
            resultado['situacao'] = 'Razoavel'
        else:
            resultado['situacao'] = 'Ruim'

    return resultado

#Programa Principal
resposta = lnota(4, 7, 10, 5.5, 4, situacao=True)
print(resposta)