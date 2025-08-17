def area(a, b):
    are = a*b
    print('-'*40)
    print(f'A area de um terreno {a}x{b} é: {are}M²')


#Programa principal
print('{:-^40}'.format('Area Terreno'))
area(a= float(input('largura (M): ')), b=float(input('Comprimento (M): ')))
