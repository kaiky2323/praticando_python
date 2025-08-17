km = int(input('Qual a distancia da viagem?: '))
print("Você esta prestes a começar uma viagem de {}KM".format(km))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))