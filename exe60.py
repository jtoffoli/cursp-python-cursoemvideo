termo = int(input('digite o primeiro termo da razão: '))
razão = int(input('digite a razão da PA: '))
i = 0
pa = 0
while i < 10:
    pa = termo + (razão*i)
    print(f'{pa}',end='')
    print(' -> ' if i < 10 else '',end ='' )
    i += 1
print('FIM')