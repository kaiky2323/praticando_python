peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso/(altura * altura)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
print('Você esta na faixa de peso: ', end='')
if imc < 18.5:
    print('Abaixo do peso ')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc >= 25.1 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30.1 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')