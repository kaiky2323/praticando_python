#ler o nome e o preço de um produto
#quer continuar?
#mostrar o total da comprar
#quantos produtos acima de mil reais
#o nome do produto mais barato
cont = preco = total = menor_prod = maior_prod = menor_preco = 0
resp =''
print('{:=^40}'.format('Compre mais'))
while True:
    cont += 1
    nomep = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        maior_prod += 1
    if cont == 1:
        menor_preco += preco
    else:
        if preco < menor_preco:
            menor_preco = preco
            menor_prod = nomep
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da comprar foi R${total:.2f}')
print(f'Temos {maior_prod} custando mais de R$1.000,00')
print(f'O produto masi barato foi {menor_prod} que custa R${menor_preco:.2f}')