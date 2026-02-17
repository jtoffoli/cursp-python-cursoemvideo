def soma(a=0,b=0,c=0):
    """
    Uma função que recebe 3 parâmetros e retorna
    a soma deles
    :param a: número
    :param b: número
    :param c: número
    :return: 'sem retorno
    """
    s = a + b + c
    print(f'A soma dos valores é {s}')
help(soma)
soma(1,2,3)
soma(4,5)
soma(8)
soma()