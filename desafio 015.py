d = int(input("quantos dias alugados? "))
sd = d * 60
km = int(input("Quantos KMs rodados? "))
skm = km * 0.15
print("Dias alugados: {}.\nKMs rodados: {}.\nTotal a pagar pelo aluguel: R${}".format(d, km, sd + skm ))