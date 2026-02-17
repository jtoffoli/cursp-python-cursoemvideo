from random import randint
from time import sleep
números = list()
def sorteia(lst):
    print('sorteando 5 valores da lista: ', end='')
    for i in range(0,5):
        sleep(0.5)
        i = randint(1, 50)
        números.append(i)
        print(i, end=' ')
    print('PRONTO!')
def somapar(lst):
    soma = 0
    for i in lst:
        if i % 2 == 0:
            soma+=i
    print(f'Somando os valores pares de {números}, temos {soma}')
sorteia(números)
somapar(números)
