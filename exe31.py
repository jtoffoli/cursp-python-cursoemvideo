cores = {'vermelho' : '\033[1;31m' , 'limpa' : '\033[m' , 'roxo' : '\033[1;35m'}
salario = float(input('{}digite seu salário:R${}'.format(cores['roxo'] , cores['limpa'])))
if salario <= 1250.0:
    aumento = salario * 0.15
    print(f'{cores['vermelho']}quem ganhava R${salario} passa a ganhar R${salario + aumento:.2f}{cores['limpa']}')
elif salario > 1250.0:
    aumento = salario * 0.10
    print(f'{cores['vermelho']}quem ganhava R${salario} passa a ganhar {salario + aumento:.2f}{cores['limpa']}')