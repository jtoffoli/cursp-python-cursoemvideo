termo = int(input('digite o primeiro termo da razão: '))
razão = int(input('digite a razão da PA: '))
i = 1
pa = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while i < total:
        pa = termo + (razão*i)
        print(f'{pa}',end='')
        print(' -> ' if i < total else '',end ='' )
        i += 1
    print('PAUSA')
    mais = int(input('Quantos termos voçê quer mostrar a mais? '))
print('FIM')
print('{} termos mostrados'.format(total))