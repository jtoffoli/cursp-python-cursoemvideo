num = int(input('digite um número: '))
cont = num-1
fatorial = num
print(f'{fatorial}! = {fatorial} X ',end= '')
while cont > 0:
    print(cont,end='')
    print(f' X 'if cont > 1 else ' = ',end='')
    num *= cont
    cont -= 1
print(num)
# resolução com for
num = int(input('digite o número que voçê quer ver o fatorial: '))
i = num-1
print('{}! = {} '.format(num,num),end='')
for i in range(i,0,-1):
    print(f' x  {i} ',end='')
    num *= i
print(' = {}'.format(num),end='')