num = int(input('digite um número: '))
cont = 0
for i in range (1,num+1):
    if num % i == 0:
        print('\033[33m',end=' ')
        cont+=1
    else:
        print('\033[31m',end=' ')
    print(i,end=' ')
print('\033[m\no número {} foi dividido {} vezes'.format(num,cont,))
if cont == 2:
    print('o número {} é primo'.format(num))
else:
    print('o número {} não é primo.'.format(num))