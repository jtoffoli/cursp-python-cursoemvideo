n = int(input('Didite a quantidade de termos sa sequência: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} -> {t2} -> ',end='')
while cont <= n:
    t3 = t2 + t1
    print(f'{t3} -> ',end='')
    t1 = t2
    t2 = t3
    cont+=1
print('FIM')