n1 = int(input('digite um valor: '))
n2 = int(input('digite um valor: '))
n3 = int(input('digite um valor: '))
maior = n1
menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'o maior valor é {maior} e o menor valor é {menor}')
