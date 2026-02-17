print('-'*30)
print('JOGO DA MEGASENA')
print('-'*30)
from random import randint
from time import sleep
palpite = list()
lista = list()
num = int(input('Digite a quantidade de palpites que voçê deseja: '))
print(f'{'Sorteando {} jogos':-^25}'.format (num))
for num in range(0,num):
    for i in range(0,6):
        palpite.append(randint(1,60))
        palpite.sort()
    if palpite in lista:
        for i in range(0, 6):
            palpite.append(randint(1, 60))
            palpite.sort()
    lista.append(palpite[:])
    palpite.clear()
for i in range(0,len(lista)):
    print(f'lista {i+1}')
    print(lista[i])
    sleep(1)
print(f'{'BOA SORTE':>^25}')
