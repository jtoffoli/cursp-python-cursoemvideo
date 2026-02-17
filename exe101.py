def fatorial(n,show=False):
    '''
    --> calcula o fatorial de um numero
    :param n: o número a ser calculado o fatorial
    :param show: se a conta do fatorial vai ser mostrada ou não
    :return: o valor do fatorial do número escolhido
    '''
    f = 1
    for i in range(n,0,-1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
            f*=i
    return f
num = int(input('Digite um número para ver seu fatorial: '))
print(fatorial(num, True))