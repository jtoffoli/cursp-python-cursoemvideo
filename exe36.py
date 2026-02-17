cores = {'vermelho':'\033[1;31m', 'roxo' : '\033[1;35m', 'limpa' : '\033[m', 'azul': '\033[1;36m'}
v1 = int(input(f'{cores['azul']}digite um valor qualquer: {cores['limpa']}'))
v2 = int(input(f'{cores['azul']}digite outro valor qualquer: {cores['limpa']}'))
if v1 == v2:
    print(f'{cores['roxo']}não existe valor maior, ambos são iguais.{cores['limpa']}')
elif v1 > v2:
    print(f'{cores['vermelho']}o valor 1 é maior que o valor 2{cores['limpa']}')
else:
    print(f'{cores['vermelho']}o valor 2 é maior que o valor 1{cores['limpa']}')