expressao = str(input('Digite uma expressão: '))
identificador = []

for simbolo in expressao:
    if simbolo == '(':
        identificador.append('(')
    elif simbolo == ')':
        if  len(identificador) > 0:
            identificador.pop()
        else:
            identificador.append(')')
            break
if len(identificador) == 0:
    print('Sua expressão esta valida!!')
else:
    print('Sua expressão é invalida!!')