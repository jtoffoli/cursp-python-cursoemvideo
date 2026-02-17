matriz = [[int(input(f'Digite um valor para {[y]} {[x]}: ')) for x in range(3)] for y in range(3)]
soma1 = soma2 = maior = 0
for i in range(0,len(matriz)):
    for j in range(0,len(matriz)):
        print(f'{[ matriz[i][j] ]}',end=' ')
    print('\n')
for i in range(0,len(matriz)):
    for j in range(0, len(matriz)):
        if matriz[i][j] % 2 == 0:
            soma1 += matriz[i][j]
        if j == len(matriz) - 1:
            soma2+=matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]
print(f'a soma dos valores pares é {soma1}')
print(f'a soma dos valores da terceira coluna é {soma2}')
print(f'O maior valor da segunda linha é {maior}')