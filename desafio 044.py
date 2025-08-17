print('{:=^40}'.format(' LOJAS TEODORO '))

preco = float(input('Valor da compra: R$'))
pagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ] A vista/ dinheiro
[ 2 ] à vista/ Cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão

Qual é a opção: '''))

if pagamento == 1:
    desconto = preco -(preco * 10)/100

elif pagamento == 2:
    desconto = preco - (preco*5)/100

elif pagamento == 3:
    pagar = preco

elif pagamento == 4:
    pagar = preco + (preco * 20)/100
    parcelas = int(input('Quantas parcelas? '))
    print('Vocẽ irar parcelar a compra em {}x '.format(parcelas), end='')

print('Voce ira pagar R${:.2f}'.format(pagar))