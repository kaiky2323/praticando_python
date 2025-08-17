from time import sleep

print('{:=^40}'.format('\033[33m TABUADA \033[m'))

numero = int(input('Qual o numero gostaria de saber a tabuada: '))
print('CALCULANDO AGUARDE...')
sleep(3)

for contador in range (0, 11):
    multiplicador = numero * contador
    print(numero, 'X', contador, '=', multiplicador )