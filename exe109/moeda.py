def metade(preco = 0, formato = False):
    res = preco/2
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato = False):
    res = preco*2
    return res if formato is False else moeda(res)

def aumentar(preco = 0,x=0,formato = False):
    res = (preco/100*x)+preco
    return res if formato is False else moeda(res)

def reduzir(preco = 0,x=0, formato = False):
    res = preco-(preco/100*x)
    return res if formato is False else moeda(res)

def moeda (preco = 0,moeda='R$', formato = False):
    res = f'{moeda}{preco:.2f}'.replace('.',',')