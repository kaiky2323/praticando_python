
nome = str (input('Digite seu nome completo: ')).strip()
print('Analizando seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
divisor = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(divisor[0], len(divisor[0])))