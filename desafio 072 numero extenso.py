
extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis",
           "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze",
           "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

num = int(input('digite um numero entre 0 e 20: '))
while True:
    if num >= 21 or num <= -1:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    else:
      break
print(f'Você digitou o numero {extenso[num]}')