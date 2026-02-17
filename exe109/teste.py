from exe109 import moeda

p = float(input('Digite o preço:R$ '))
print(f'A metade de {p} é {moeda.metade(p,True)}')
print(f'o dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10, True)}')
print(f'reduzindo 13%, temos {moeda.reduzir(p,13, True)}')