def resumo(p=0,aumento=0,reducao=0):
    print('-'*30)
    print(f'{'RESUMO DO VALOR'}')
    print('-' * 30)
    print(f'Preço analisado: R${p}')
    print(f'Dobro do preço: {dobro(p, True)}')
    print(f'{aumento}% de aumento temos: {aumentar(p, aumento, True)}')
    print(f'{reducao}% de redução: {reduzir(p,reducao,True)}.')
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
    return res