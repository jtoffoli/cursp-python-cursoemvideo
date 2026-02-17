import random
n1 = str(input('digite um nome : \n'))
n2 = str(input('digte um nome: \n'))
n3 = str(input('gidite um nome : \n'))
n4 = str(input('dgite um nome : \n'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(' a ordem escolhida foi {}'. format(lista))