import random
n1 = str(input("Digite o primeiro nome: "))
n2 = input("Digite o segundo nome: ")
n3 = input("Digite o terceiro nome: ")
lista = [n1, n2, n3]
win = random.choice(lista)
print ("O aluno vencedor do sorteio foi: {}".format(win))