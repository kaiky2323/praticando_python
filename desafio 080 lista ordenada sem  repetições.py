lista = []
for contador in range(0,5):
    numero = int(input('Digite um numero: '))
    if contador == 0 or  numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado a posição {pos}')
                break
            pos += 1

print(lista)