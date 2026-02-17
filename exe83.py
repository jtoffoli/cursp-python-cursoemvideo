lista =  [[],[]]
for i in range(0,7):
    num = (int(input(f'Digite o {i+1} valor: ')))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
if lista[0][0] % 2 == 0:
    print(f'Os valores pares em ordem crescente são: {lista[0]}')
    print(f'Os valores ímpares em ordem crescente são: {lista[1]}')
    print(f'a lista de todos os valores é: {lista}')
else:
    print(f'Os valores ímpares em ordem crescente são: {lista[0]}')
    print(f'Os valores pares em ordem crescente são: {lista[1]}')
    print(f'a lista de todos os valores é: {lista}')