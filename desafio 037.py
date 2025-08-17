from opbinario.opbinario import opbinario

numero = int(input("digite algum valor: "))
print("""[1] converter para BINÁRIO
[2] converter para OCTAL 
[3] converter para HEXADECIMAL""")
opcao = int(input('Sua opção: '))

#criando as variaveis
binar = opbinario.bin(numero)
octal = opbinario.oct(numero)
hexa = opbinario.hex(numero)

#Criando as escolhas
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, binar))
elif opcao == 2:
    print('{} coonvertido para OCTAL é igual a {}'.format(numero, octal))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hexa))
else:
    print('\033[31mOPÇÃO INVALIDA!!!\033[m')