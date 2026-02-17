soma = 0
for i in range (0,6):
    num = int(input('digite um valor: '))
    if num % 2 == 0:
        soma += num
print('a soma dos números inteiros pares é: {}'.format(soma))