from time import sleep
def maior(*num):
    cont = maiorNum = 0
    print('Analisando os valores passados.')
    for n in num:
        print(f'{n} ', end='')
        if n > maiorNum:
            maiorNum = n
        cont += 1
        sleep(0.5)
    print(f'\nforam passados {cont} valores e o maior é {maiorNum}.')
maior()