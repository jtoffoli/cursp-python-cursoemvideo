tupla = (int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')))
print(f'Valores digitados: {tupla}',end='')
print(f'\nO valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3)+1}º posição.')
else:
    print('O valor 3 não apareceu na tupla')
print('Os valores pares são: ',end=' ')
for i in tupla:
    if i % 2 == 0:
        print(i,end = ' ')