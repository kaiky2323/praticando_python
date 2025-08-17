import math
catO = int(input("Qual o comprimento do cateto oposto: "))
catA = int(input("Qual o comprimento do cateto adjacente: "))
hip = (catO**2) + (catA**2)
hipo = math.sqrt(hip)
print("\033[36;47mO valor da hipotenusa desse triangulo é {}\033[m".format(hipo))