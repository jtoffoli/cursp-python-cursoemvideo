cores = {'vermelho':'\033[1;31m', 'roxo' : '\033[1;35m', 'limpa' : '\033[m', 'azul':'\033[1;34m'}
casa = float(input(f'{cores['roxo']} qual o valor da casa? {cores['limpa']}'))
salario = float(input('{} qual seu salário?R${}'.format(cores['roxo'],cores['limpa'])))
anos = float(input('{} em quantos anos voçê pretende pagar a casa?{}'.format(cores['roxo'],cores['limpa'])))
prestacao = casa / (anos*12)
porcentagem = salario / 100 * 30
if prestacao > porcentagem:
    print(f'{cores['vermelho']}ERRO!! Empréstimo negado! motivo, o valor da prestação excede 30% do salário informado, valor da parcela mensal {prestacao:.2f}{cores['limpa']}')
else:
    print(f'{cores['azul']}Empréstimo aceito, valor da parcela mensal: {prestacao:.2f}{cores['limpa']}')