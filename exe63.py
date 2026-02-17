num = cont = soma = 0
while num != 999:
    num = int(input('digite um numero: '))
    if num != 999:
        soma += num
        cont += 1
print('foram digitados {} números e a soma entre eles é de {}'.format(cont, soma))