from time import sleep
def contador(i,f,p):
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print(f'contagem de {i} até {f} de {p} em {p}!')
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
            sleep(0.5)
        print('FIM!!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
            sleep(0.5)
        print('FIM!!')
contador(1,10,1)
contador(10,0,2)
print('Contagem personalizada')
ini = int(input('ínicio: '))
fim = int(input('Fim: '))
pace = int(input('passo: '))
contador(ini, fim, pace)

