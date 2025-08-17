sexo = str(input('Digite seu sexo F/M ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos por favor digite seu sexo: ')).upper().strip()[0]
print('sexo {} registrado com sucesso!!!'.format(sexo))