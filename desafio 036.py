Vcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int (input('Vai pagar em quantos anos? '))
meses = anos*12
pagar = Vcasa/meses
if pagar >= (30/100)*salario:
    print("""\033[31mEMPRESTIMO NEGADO\033[m
    o emprestimo ultrapassa 30% do seu salario
    com R${:.2f}""".format(pagar))
else:
    print("""\033[32mEMPRESTIMO APROVADO!!!\033[m
    Você ira pagar em {} anos R${:.2f} por mes ate la""".format(anos, pagar))