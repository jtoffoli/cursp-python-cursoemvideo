continuar = ' '
cont = soma = maior = menor = 0
while continuar[0] != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    continuar = str(input('Voçê quer continuar a digitar números [sim/não]: ')).strip().upper()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    if continuar[0] == 'N':
        print('Programa encerrado')
print('A média de todos os valores digitados é {:.2f}'.format(soma/cont))
print('O maior valor é {} e o menor valor é {}'.format(maior,menor))