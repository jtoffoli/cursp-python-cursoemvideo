def metade(n = 0):
    res = n/2
    return res

def dobro(n = 0):
    res = n*2
    return res

def aumentar(n = 0,x=0):
    res = (n/100*x)+n
    return res

def reduzir(n = 0,x=0):
    res = n-(n/100*x)
    return res

def moeda (preco = 0,moeda='R$'):
    res = f'{moeda}{preco:.2f}'.replace('.',',')
    return res