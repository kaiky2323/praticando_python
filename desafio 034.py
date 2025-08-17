salario = float(input('Qual é o salario do funcionário? R$'))
maior = salario + (15*salario)/100
menor = salario + (10*salario)/100
if salario <= 3000:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, maior))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, menor))